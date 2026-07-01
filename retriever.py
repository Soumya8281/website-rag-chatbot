import json
import faiss
from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query):

    # Load FAISS index
    index = faiss.read_index("website.index")

    # Load text chunks
    with open("chunks.json", "r", encoding="utf-8") as file:
        chunks = json.load(file)

    # Convert question to embedding
    query_embedding = model.encode([query]).astype("float32")

    # Search the vector database
    distances, indices = index.search(query_embedding, k=1)

    # Return the most relevant chunk
    return chunks[indices[0][0]]