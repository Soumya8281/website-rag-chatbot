from scraper import scrape_website
from chunker import chunk_text
from vector_store import create_vector_store
from retriever import retrieve
from gemini_chat import ask_gemini

# Get website URL
url = input("Enter Website URL: ")

# Scrape website
scrape_website(url)

# Create chunks
chunk_text("website.txt")

# Create vector database
create_vector_store()

# Ask user question
question = input("\nAsk your question: ")

# Retrieve relevant chunk
context = retrieve(question)

# Generate answer using Gemini
answer = ask_gemini(context, question)

print("\n🤖 Answer:\n")
print(answer)