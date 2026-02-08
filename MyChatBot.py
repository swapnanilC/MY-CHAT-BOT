import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.header("SWAPNANIL'S BOT")

with st.sidebar:
    st.title("My notes")
    file = st.file_uploader("Choose a PDF", type="pdf")

if file is not None:
    pdf = PdfReader(file)
    text = ""

    for page in pdf.pages:
        if page.extract_text():
            text += page.extract_text()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,
        chunk_overlap=20
    )

    chunks = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"
    )

    vector_store = FAISS.from_texts(chunks, embeddings)

    st.success("PDF indexed successfully!")

    user_query = st.text_input("Ask a question")

    llm = OllamaLLM(
        model="tinyllama",
        temperature=0.2,
        num_ctx=1024
    )

    if user_query:
        docs = vector_store.similarity_search(user_query, k=2)
        context = "\n\n".join(doc.page_content for doc in docs)

        prompt = ChatPromptTemplate.from_template(
            """
            Answer using ONLY the context below.
            If not found, say "I don't know".

            Context:
            {context}

            Question:
            {question}
            """
        )

        chain = prompt | llm | StrOutputParser()

        response = chain.invoke({
            "context": context,
            "question": user_query
        })

        st.write("### Answer")
        st.write(response)
