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

1.Python

2.Streamlit

3.LangChain

4.FAISS

5.HuggingFace Sentence Transformers

6.Ollama (TinyLLaMA)

7.PyPDF2

📂 Project Workflow

1.Upload a PDF file

2.Extract text from the document

3.Split text into chunks

4.Generate embeddings using HuggingFace models

5.Store vectors in FAISS

6.Retrieve relevant chunks for a query

7.Generate answers using a local LLM

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
