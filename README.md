# 📈 Agentic Financial Intelligence Platform

> An end-to-end **Multi-Agent AI Financial Document Analysis Platform** built using **LangGraph**, **Retrieval-Augmented Generation (RAG)**, **FastAPI**, **Streamlit**, **PostgreSQL**, **ChromaDB**, and **Docker**.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql)

---

# 🚀 Overview

The **Agentic Financial Intelligence Platform** is an AI-powered financial document analysis system capable of understanding SEC filings, annual reports, quarterly reports, and other financial documents using a collaborative team of specialized AI agents.

Unlike traditional RAG systems, this project employs a **LangGraph Multi-Agent architecture** where independent AI agents plan, retrieve, analyze, validate, and synthesize information before producing a final executive summary.

The platform also maintains secure user authentication, conversation history, execution traces, metadata extraction, and persistent document embeddings for scalable financial intelligence.

---

# ✨ Features

### 🤖 Multi-Agent AI Workflow

- Supervisor Agent
- Planner Agent
- Research Agent
- Financial Analyst Agent
- Reflection Agent
- Answer Generation Agent

---

### 📄 Financial Document Intelligence

Supports analysis of:

- Annual Reports (10-K)
- Quarterly Reports (10-Q)
- Financial Statements
- Company Reports
- SEC Filings

---

### 🔍 Retrieval Augmented Generation (RAG)

- ChromaDB Vector Database
- Hybrid Semantic Retrieval
- Recursive Text Chunking
- Metadata-aware Search
- Persistent Embeddings

---

### 🧠 AI Capabilities

- Executive Summaries
- Financial Risk Analysis
- Revenue & Profit Analysis
- Business Strategy Insights
- Company Performance Evaluation
- Multi-document Reasoning

---

### 🔐 Authentication

- JWT Authentication
- Secure Password Hashing
- User Registration
- Login
- Protected APIs

---

### 💬 Conversation Management

- Persistent Chat History
- Previous Conversation Retrieval
- Conversation Deletion
- PostgreSQL Storage

---

### 📊 Rich Dashboard

- AI Response
- Agent Execution Trace
- Document Metadata
- Executive Summary
- Conversation History
- Markdown Export

---

### 🐳 Production Ready

- Dockerized Backend
- Dockerized Frontend
- PostgreSQL Container
- Environment Variables
- Docker Compose Deployment

---

# 🏗 System Architecture

```
                User
                  │
                  ▼
          Streamlit Frontend
                  │
                  ▼
            FastAPI Backend
                  │
          JWT Authentication
                  │
                  ▼
         LangGraph Multi-Agent
                  │
   ┌──────────────┼──────────────┐
   ▼              ▼              ▼
Planner      Researcher     Financial Analyst
   │              │              │
   └──────────────┼──────────────┘
                  ▼
          Reflection Agent
                  │
                  ▼
            Answer Generator
                  │
        Hybrid RAG Retrieval
                  │
          Chroma Vector DB
                  │
          Financial Documents
                  │
          PostgreSQL Database
```

---

# 🧠 Multi-Agent Workflow

```
User Question

      │

      ▼

Supervisor

      │

      ▼

Planner

      │

      ▼

Research Agent

      │

      ▼

Financial Analyst

      │

      ▼

Reflection Agent

      │

      ▼

Answer Generator

      │

      ▼

Final Executive Summary
```

---

# 📁 Project Structure

```
agentic-financial-intelligence-platform

│

├── app/
│   ├── agents/
│   ├── api/
│   ├── auth/
│   ├── database/
│   ├── graph/
│   ├── llm/
│   ├── rag/
│   ├── schemas/
│   └── main.py
│
├── frontend/
│   ├── assets/
│   ├── components/
│   ├── services/
│   ├── styles/
│   ├── utils/
│   ├── views/
│   └── app.py
│
├── docker/
│
├── data/
│   ├── uploads/
│   ├── processed/
│   └── chroma_db/
│
├── docs/
│
├── tests/
│
├── requirements.txt
├── README.md
└── docker-compose.yml
```

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- LangGraph
- LangChain
- ChromaDB
- JWT Authentication

---

## Frontend

- Streamlit
- Requests
- HTML/CSS

---

## AI

- OpenRouter
- LangChain
- Sentence Transformers
- Hybrid Retrieval
- Multi-Agent Reasoning

---

## Infrastructure

- Docker
- Docker Compose

---

# ⚡ Installation

## Clone

```bash
git clone https://github.com/YOUR_USERNAME/agentic-financial-intelligence-platform.git

cd agentic-financial-intelligence-platform
```

---

## Environment Variables

Create

```
.env.docker
```

Example

```env
OPENROUTER_API_KEY=YOUR_KEY

OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

OPENROUTER_MODEL=poolside/laguna-m.1:free

DATABASE_URL=postgresql://postgres:password@postgres:5432/agentic_ai

JWT_SECRET_KEY=your_secret

JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# 🐳 Docker

Run the entire platform

```bash
docker compose -f docker/docker-compose.yml up --build
```

Frontend

```
http://localhost:8501
```

Backend

```
http://localhost:8000/docs
```

---

# 📸 Screenshots

## 📊 Dashboard

![Dashboard](docs/images/dashboard.png)

---

## 🤖 AI Response

![AI Response](docs/images/answer.png)

---

## ⚙ Agent Execution

### Execution Trace - Part 1

![Execution Trace 1](docs/images/execution_trace_1.png)

### Execution Trace - Part 2

![Execution Trace 2](docs/images/execution_trace_2.png)

# 🔄 Example Workflow

```
User Question

↓

Planner Agent

↓

Research Agent

↓

Retrieve Relevant Chunks

↓

Financial Analysis

↓

Reflection

↓

Executive Summary

↓

Conversation Saved
```

---

# 📌 Future Improvements

- PDF Upload Support
- Real-time Streaming Responses
- Multi-document Comparison
- Financial Charts
- Portfolio Analysis
- Stock Market Integration
- OCR Support
- User Roles & Permissions
- Kubernetes Deployment
- CI/CD Pipeline
- Redis Caching

---

# 👨‍💻 Author

**Vishwa Nayani**

GitHub: https://github.com/vishwayani
