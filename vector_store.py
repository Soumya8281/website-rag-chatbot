import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store():

    # Read chunks
    with open("chunks.json", "r", encoding="utf-8") as file:
        chunks = json.load(file)

    # Create embeddings
    embeddings = model.encode(chunks)

    # Convert to numpy array
    embeddings = np.array(embeddings).astype("float32")

    # Create FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])

    # Add embeddings
    index.add(embeddings)

    # Save FAISS index
    faiss.write_index(index, "website.index")

    print(f"✅ Stored {len(chunks)} chunks in FAISS.")