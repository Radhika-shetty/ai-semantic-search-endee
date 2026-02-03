from sentence_transformers import SentenceTransformer
import numpy as np
import os

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample documents (later can be PDF / DB / API)
documents = [
    'Artificial Intelligence is transforming industries.',
    'Machine Learning allows systems to learn from data.',
    'Endee is used as a vector database for semantic search.',
    'Semantic search finds meaning, not just keywords.'
]

# Create embeddings
embeddings = model.encode(documents)

# Save embeddings (simulating vector DB storage)
os.makedirs('data', exist_ok=True)
np.save('data/embeddings.npy', embeddings)
np.save('data/documents.npy', np.array(documents))

print('✅ Documents embedded and stored successfully')
