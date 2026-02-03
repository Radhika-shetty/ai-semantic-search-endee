# src/load_docs.py
import os
import shutil

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def add_document(filename: str, content: str):
    """
    Adds a new document to data/ folder and saves it as a .txt file.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    file_path = os.path.join(DATA_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Document '{filename}' added successfully to {DATA_DIR}")

if __name__ == "__main__":
    # Example usage: edit here to add new document
    doc_name = "new_doc.txt"
    doc_content = "This is the content of the new document about AI and semantic search."
    add_document(doc_name, doc_content)
