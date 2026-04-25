from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import TypedDict, List
from langchain_community.llms import Ollama
from langgraph.graph import StateGraph

# -------------------------
# STEP 1: Load PDF
# -------------------------
loader = PyPDFLoader("Customer_Support.pdf")
documents = loader.load()

# -------------------------
# STEP 2: Chunking
# -------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

print(f"Chunks created: {len(chunks)}")

# -------------------------
# STEP 3: Embeddings
# -------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -------------------------
# STEP 4: Vector Store
# -------------------------
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./chroma_db"
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# -------------------------
# STEP 5: LLM
# -------------------------

llm = Ollama(model="llama3")

# -------------------------
# STATE (IMPORTANT)
# -------------------------
class GraphState(TypedDict, total=False):
    query: str
    docs: List
    route: str
    answer: str


# -------------------------
# NODE 1: Retrieve
# -------------------------
def retrieve_node(state):
    query = state.get("query", "")

    docs = retriever.invoke(query)

    if not docs:
        return {"docs": [], "route": "human"}

    return {"docs": docs, "route": "process"}


# -------------------------
# NODE 2: Decide (Routing)
# -------------------------
def decision_node(state):
    query = state.get("query", "")
    docs = state.get("docs", [])

    keywords = ["enterprise", "legal", "compliance", "complaint", "complex"]

    if any(word in query.lower() for word in keywords):
        return {"route": "human"}

    if not docs:
        return {"route": "human"}

    return {"route": "llm"}


# -------------------------
# NODE 3: LLM Response
# -------------------------
def llm_node(state):
    docs = state.get("docs", [])
    query = state.get("query", "")

    context = " ".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a helpful customer support assistant.

    Answer the question in 1-2 clear sentences.
    Do NOT repeat the question.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    response = llm.invoke(prompt)

    return {"answer": response.strip()}

# -------------------------
# NODE 4: Human (HITL)
# -------------------------
def human_node(state):
    print("\nEscalated to Human Support")
    human = input("Enter human response: ")
    return {"answer": human}


# -------------------------
# BUILD GRAPH
# -------------------------
graph = StateGraph(GraphState)

graph.add_node("retrieve", retrieve_node)
graph.add_node("decision", decision_node)
graph.add_node("llm", llm_node)
graph.add_node("human", human_node)

# Flow
graph.set_entry_point("retrieve")

graph.add_edge("retrieve", "decision")

graph.add_conditional_edges(
    "decision",
    lambda state: state["route"],
    {
        "llm": "llm",
        "human": "human"
    }
)

graph.set_finish_point("llm")
graph.set_finish_point("human")

# Compile
app = graph.compile()

# -------------------------
# RUN LOOP
# -------------------------
while True:
    query = input("\nAsk your question (or 'exit'): ")

    if query.lower() == "exit":
        break

    result = app.invoke({"query": query})
    print("\nFinal Answer:", result["answer"])