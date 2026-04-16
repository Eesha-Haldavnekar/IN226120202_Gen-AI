# AI Resume Screening System with LangChain

## 📌 Project Overview

This project implements an **AI-powered Resume Screening System** that evaluates candidate resumes against a job description.
The system extracts skills, matches them with required skills, assigns a score, and provides an explanation.

## 🎯 Objective

* Build an AI-based resume evaluation system
* Use LangChain for pipeline creation
* Provide scoring + explainability
* Demonstrate automated candidate filtering

## 🛠️ Tech Stack

* Python
* LangChain
* HuggingFace Transformers
* Jupyter Notebook

## ⚙️ Features

* Resume skill extraction
* Skill matching with job description
* Automatic scoring (0–100)
* Explanation generation
* Strong vs Weak candidate comparison


## 🚀 How It Works

1. Input candidate resume
2. Extract skills from resume
3. Compare with required job skills
4. Calculate matching score
5. Generate explanation

## 📊 Example Output

### Strong Candidate

```
Score: 85
Matched Skills: python, machine learning, pandas, numpy, scikit-learn, sql
Explanation: Candidate matched 6 out of 7 required skills.
```

### Weak Candidate

```
Score: 0
Matched Skills: None
Explanation: Candidate matched 0 out of 7 required skills.
```

## 🧠 Evaluation Logic

```
Score = (Matched Skills / Total Required Skills) * 100
```

## 📌 Future Improvements

* Resume PDF parsing
* LLM-based skill extraction
* UI using Streamlit
* Database integration

## 👩‍💻 Author

Eesha Haldavnekar
Third Year Computer Engineering

## 📄 License

This project is for academic use.
