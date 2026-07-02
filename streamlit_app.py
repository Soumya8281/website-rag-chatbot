import streamlit as st

from scraper import scrape_website
from chunker import chunk_text
from vector_store import create_vector_store
from retriever import retrieve
from gemini_chat import ask_gemini

st.set_page_config(page_title="Website RAG Chatbot")

st.title("🤖 Website RAG Chatbot")

st.write("Ask questions based on any website.")

if "processed" not in st.session_state:
    st.session_state.processed = False

website_url = st.text_input(
    "Enter Website URL",
    placeholder="https://www.python.org"
)

if st.button("Process Website"):

    if website_url:

        with st.spinner("Processing website..."):

            scrape_website(website_url)
            chunk_text("website.txt")
            create_vector_store()

        st.session_state.processed = True

        st.success("Website processed successfully!")

    else:
        st.warning("Please enter a website URL.")

if st.session_state.processed:

    question = st.text_input(
        "Ask a Question",
        placeholder="What is Python?"
    )

    if st.button("Get Answer"):

        if question:

            with st.spinner("Generating answer..."):

                context = retrieve(question)
                answer = ask_gemini(context, question)

            st.subheader("Answer")

            st.write(answer)

        else:
            st.warning("Please enter a question.")