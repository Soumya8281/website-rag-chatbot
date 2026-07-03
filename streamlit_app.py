# Professional Streamlit UI for Website RAG Chatbot
# Replace your existing streamlit_app.py with this file.

import time
import streamlit as st

from scraper import scrape_website
from chunker import chunk_text
from vector_store import create_vector_store
from retriever import retrieve
from gemini_chat import ask_gemini

st.set_page_config(
    page_title="Website RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.main {background-color:#0E1117;}
.hero{
padding:25px;
border-radius:18px;
background:linear-gradient(90deg,#4F46E5,#0EA5E9);
color:white;
margin-bottom:25px;
}
.answer{
background:#1F2937;
padding:18px;
border-radius:12px;
border-left:6px solid #38BDF8;
}
.metric-card{
background:#161B22;
padding:12px;
border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

if "processed" not in st.session_state:
    st.session_state.processed=False

if "history" not in st.session_state:
    st.session_state.history=[]

with st.sidebar:
    st.title("🤖 Website RAG")
    st.markdown("### About")
    st.write("Ask questions from any website using Retrieval-Augmented Generation.")
    st.markdown("---")
    st.markdown("### Tech Stack")
    st.markdown("""
- Python
- BeautifulSoup
- Sentence Transformers
- FAISS
- Google Gemini
- Streamlit
""")
    st.markdown("---")
    if st.button("🗑 Clear Chat"):
        st.session_state.history=[]
    

st.markdown("""
<div class="hero">
<h1>🤖 Website RAG Chatbot</h1>
<p>AI-powered website question answering using RAG, FAISS and Gemini.</p>
</div>
""", unsafe_allow_html=True)

c1,c2,c3=st.columns(3)
c1.metric("🤖 AI Model","Gemini")
c2.metric("🗄️ Vector Database","FAISS")
c3.metric("🧠 Embedding Model","MiniLM")

st.divider()

st.header("🌐 Step 1 - Process Website")
st.info(
    "Enter a public website URL and click **Process Website** before asking questions."
)

website_url=st.text_input(
    "Website URL",
    placeholder="https://www.python.org"
)

if st.button("🚀 Process Website", use_container_width=True):

    if not website_url:
        st.warning("Please enter a website URL.")
    else:
        start=time.time()
        progress=st.progress(0,text="🔍 Scraping website...")
        scrape_website(website_url)

        progress.progress(35,text="✂️ Chunking website...")
        chunk_text("website.txt")

        progress.progress(70,text="🧠 Creating embeddings...")
        create_vector_store()

        progress.progress(100, text="✅ Website processed successfully!")

        st.session_state.processed=True

        st.success(f"✅ Website processed successfully in {time.time()-start:.2f} seconds.")

st.divider()

if st.session_state.processed:

    st.header("💬 Step 2 - Ask Questions")

    question=st.text_input(
        "Question",
        placeholder="Example: What is Python used for?"
    )

    if st.button("🤖 Get Answer", use_container_width=True):

        if not question:
            st.warning("Please enter a question.")
        else:
            start=time.time()

            with st.spinner("🤖 Generating answer using Gemini..."):
                context=retrieve(question)
                answer=ask_gemini(context,question)

            elapsed=time.time()-start
            st.success("✅ Answer generated successfully!")

            st.session_state.history.append({
                "question":question,
                "answer":answer,
                "context":context,
                "time":elapsed
            })

    for chat in reversed(st.session_state.history):

        st.markdown(f"### 🙋 {chat['question']}")

        st.subheader("🤖 AI Answer")

        st.markdown(
            f'<div class="answer">{chat["answer"]}</div>',
            unsafe_allow_html=True
        )

        

        col1,col2=st.columns([4,1])
        col2.metric("⏱ Time",f"{chat['time']:.2f}s")

        with st.expander("📄 View Retrieved Context"):
            st.write(chat["context"])

        st.divider()

else:
    st.info("Process a website before asking questions.")

st.markdown("---")

st.caption(
    "Developed by **Soumya S Nair** | "
    "ClaySys AI Hackathon 2026 | "
    "Python • FAISS • Google Gemini • Streamlit"
)