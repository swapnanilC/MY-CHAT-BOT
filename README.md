📄 PDF-Based AI Chatbot (RAG)

A simple PDF-based AI chatbot built using Streamlit, LangChain, FAISS, and Ollama.
Upload any PDF and ask questions — the chatbot answers only from the document content using Retrieval-Augmented Generation (RAG).
Runs fully offline with a local LLM (TinyLLaMA), no paid APIs required.

🚀 Features

Upload and index PDF documents

Ask natural language questions based on PDF content

Context-aware answers using vector similarity search

Returns “I don’t know” if the answer is not found

Fully offline AI chatbot

Simple and interactive Streamlit UI

🛠️ Tech Stack

Python

Streamlit

LangChain

FAISS

HuggingFace Sentence Transformers

Ollama (TinyLLaMA)

PyPDF2

📂 Project Workflow

Upload a PDF file

Extract text from the document

Split text into chunks

Generate embeddings using HuggingFace models

Store vectors in FAISS

Retrieve relevant chunks for a query

Generate answers using a local LLM

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install Dependencies
pip install streamlit langchain langchain-community langchain-ollama faiss-cpu sentence-transformers PyPDF2

3️⃣ Install & Run Ollama

Download Ollama from: https://ollama.com

Pull the TinyLLaMA model:

ollama pull tinyllama

4️⃣ Run the Application
streamlit run app.py

🧠 Model Used

TinyLLaMA (via Ollama)

sentence-transformers/paraphrase-MiniLM-L3-v2 for embeddings

📌 Notes

Works completely offline after setup

Best suited for small to medium-sized PDFs

Chunk size and overlap can be tuned for better results

🎯 Future Improvements

Chat history support

Multiple PDF uploads

Source citations for answers

UI enhancements

👨‍💻 Author

Swapnanil Chakraborty
