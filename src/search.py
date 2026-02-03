# src/search.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 1: Load your documents
documents = [
    "Python is a programming language.",
    "Machine learning allows computers to learn from data.",
    "Semantic search uses embeddings to find similar text.",
    "Docker helps containerize applications."
]

# Step 2: Load a pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight and fast

# Step 3: Compute embeddings for documents
doc_embeddings = model.encode(documents)

# Step 4: Function to perform semantic search
def semantic_search(query, top_k=3):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]  # shape (n_docs,)
    
    # Get top K indices
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    # Return top documents with scores
    results = [(documents[i], float(similarities[i])) for i in top_indices]
    return results

# Step 5: Example usage
if __name__ == "__main__":
    query = "How can computers understand text?"
    results = semantic_search(query)
    print("Top results for query:", query)
    for doc, score in results:
        print(f"[Score: {score:.4f}] {doc}")
