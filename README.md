# Scientific-Moral-Debate


# 🧭 AI Moral Debate System

This is a multi-agent moral reasoning framework built using **LangGraph**, **FastAPI**, and **Streamlit**. It simulates expert agents — Neuroscientist, Psychologist, Sociologist, and Evolutionary Biologist — debating ethical dilemmas based on their disciplines, unified by a metric of **survivability**. An **Arbiter** agent then synthesizes the final conclusion.

---

## 🔍 Features

- 🧠 Scientific agents with autonomous domain-based reasoning
- 🧬 Multi-round debates: Argument → Rebuttal → Judgment
- ⚖️ Survivability-focused moral framework
- 🌐 RESTful API (FastAPI)
- 🖥️ Interactive web UI (Streamlit)
- 🧩 Modular, testable architecture

---

## 📁 Project Structure

```

LangGraph-Debate-System/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── debate.py            # FastAPI endpoint logic
│   ├── graph.py                     # LangGraph moral workflow graph
│   ├── llm/
│   │   └── agents/                  # Agent implementations (neuro, psych, socio, evobio, arbiter)
│   ├── prompts/
│   │   └── prompt.yml               # YAML-formatted prompt templates
│   └── schemas/
│       └── schemas.py               # Pydantic request/response models
├── app.py                  # Streamlit UI interface
├── .env                             # OpenAI API key (user-provided)
├── requirements.txt
├── main.py                         
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/jami78/Scientific-Moral-Debate.git
cd Scientific-Moral-Debate
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-openai-key-here
```

---

## 🚀 How to Run the System

### ✅ Step 1: Start the FastAPI Backend

```bash
uvicorn main:app --reload
```

This will host the backend at [http://localhost:8000](http://localhost:8000). You can explore the API at [http://localhost:8000/docs](http://localhost:8000/docs).

---

### 🧠 Step 2: Launch the Streamlit Interface

In a separate terminal:

```bash
streamlit run app.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Example Dilemma

> "Should a mother lie to protect her son from religious persecution?"

Each agent generates:

* **An Argument** from their scientific lens
* **A Rebuttal** to others
* A synthesized **Final Judgment** by the Arbiter

---

## 🧠 Technologies Used

* [LangGraph](https://github.com/langchain-ai/langgraph)
* [LangChain](https://www.langchain.com/)
* [OpenAI API](https://platform.openai.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Streamlit](https://streamlit.io/)
* [Pydantic](https://docs.pydantic.dev/)

---

