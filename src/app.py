# src/app.py

from src.search import semantic_search  # <-- note the src prefix

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Semantic Search API")

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

@app.post("/search")
def search_endpoint(request: QueryRequest):
    results = semantic_search(request.query, request.top_k)
    return {"query": request.query, "results": results}

@app.get("/")
def root():
    return {"message": "Semantic Search API is running!"}
