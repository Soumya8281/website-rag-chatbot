# Website RAG Chatbot

## 📌 Project Overview

This project is being developed as part of the **ClaySys AI Hackathon 2026**.

The goal is to build a Retrieval-Augmented Generation (RAG) chatbot that can answer user questions based on the content of a website.

The chatbot will:
- Scrape website content
- Extract readable text
- Split the content into smaller chunks
- Convert chunks into embeddings
- Store embeddings in a vector database
- Retrieve relevant information
- Generate answers using a Large Language Model (LLM)

---

## 🚀 Current Progress

### Milestone 1: Website Scraping ✅

Completed:
- Created the project structure
- Set up a Python virtual environment
- Installed required libraries
- Built a website scraper using `Requests` and `BeautifulSoup`
- Extracted readable text from a website
- Saved extracted content into `website.txt`

---

### Milestone 2: Text Chunking ✅

Completed:
- Implemented a text chunking module
- Split website content into smaller chunks
- Stored chunks in `chunks.json`
- Prepared the data for semantic search

---
---

### Milestone 3: Embeddings & Vector Database ✅

Completed:
- Installed Sentence Transformers and FAISS
- Generated embeddings for text chunks using the `all-MiniLM-L6-v2` model
- Converted text chunks into vector representations
- Created a FAISS vector database
- Stored embeddings for semantic search
- Saved the vector index as `website.index`

## 🛠 Technologies Used

- Python
- Requests
- BeautifulSoup
- JSON
- Sentence Transformers
- FAISS
- NumPy
- Git
- GitHub

---

## 📂 Project Structure

website-rag-chatbot/
│
├── app.py
├── scraper.py
├── chunker.py
├── vector_store.py
├── website.txt
├── chunks.json
├── website.index
├── requirements.txt
├── README.md
└── .gitignore

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/Soumya8281/website-rag-chatbot.git
```

2. Navigate to the project folder

```bash
cd website-rag-chatbot
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Run the application

```bash
python app.py
```

---

## 🔄 Upcoming Milestones

- Implement semantic search
- Integrate Gemini API
- Develop a Streamlit user interface
- Test and optimize the chatbot

---

## 👩‍💻 Developed By

**Soumya S Nair**

