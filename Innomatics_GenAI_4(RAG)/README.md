# 🤖 RAG-Based Customer Support Assistant (LangGraph + HITL)

## 📌 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** based Customer Support Assistant that answers user queries using a PDF knowledge base.

The system retrieves relevant information using embeddings and generates contextual responses using an LLM. It also includes a **Human-in-the-Loop (HITL)** mechanism to handle complex or sensitive queries.

---

## 🚀 Features
- 📄 PDF Knowledge Base Processing
- ✂️ Text Chunking & Embedding Generation
- 🧠 Semantic Search using Vector Database (ChromaDB)
- 🤖 LLM-based Answer Generation
- 🔀 Graph-based Workflow using LangGraph
- 🧑‍💻 Human-in-the-Loop (HITL) escalation for complex queries

---

## 🏗️ System Architecture

User Query  
→ Retriever (ChromaDB)  
→ Relevant Chunks  
→ LLM Processing  
→ LangGraph Decision  
→ Response / HITL Escalation  

---

## ⚙️ Tech Stack

- **Language:** Python  
- **Frameworks:** LangChain, LangGraph  
- **Vector DB:** ChromaDB  
- **Embeddings:** sentence-transformers (MiniLM)  
- **LLM:** LLaMA3 via Ollama / HuggingFace (fallback)  
- **PDF Processing:** PyPDFLoader  

---

## 🔄 Workflow

1. Load PDF document  
2. Split into chunks  
3. Convert chunks into embeddings  
4. Store embeddings in ChromaDB  
5. User enters query  
6. Retrieve relevant chunks  
7. Generate answer using LLM  
8. If query is complex → escalate to human  

---

## 🧠 LangGraph Flow

Nodes:
- `retrieve` → fetch documents  
- `decision` → route query  
- `llm` → generate answer  
- `human` → manual response  

Routing:
- Simple query → LLM  
- Complex query → HITL  

---

## 🧪 Sample Queries

### ✅ Normal Queries
- How do I reset my password?
- How can I track my order?

### 🧠 Semantic Queries
- When will I get my refund?
- How can I contact support?

### ⚠️ HITL Queries
- I have a legal compliance issue
- Enterprise billing problem

---

## 🧑‍💻 Setup Instructions

```bash
# Create virtual environment
python -m venv v.venv

# Activate environment
v.venv\Scripts\activate

# Install dependencies
pip install langchain langchain-community chromadb sentence-transformers transformers pypdf langgraph
