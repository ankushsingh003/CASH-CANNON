import chromadb
from chromadb.utils import embedding_functions
import os

def setup_rag():
    # Initialize ChromaDB persistent client
    db_path = os.path.join(os.getcwd(), "chroma_db")
    client = chromadb.PersistentClient(path=db_path)
    
    # Use a simple default embedding function
    # Note: In a production environment, you might use OpenAI or HuggingFace embeddings
    default_ef = embedding_functions.DefaultEmbeddingFunction()
    
    # Create or get the collection for Offer Mart
    collection = client.get_or_create_collection(
        name="offer_mart",
        embedding_function=default_ef
    )
    
    # Read the Offer Mart document
    with open("offer_mart.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple chunking by sections (splitting by '##')
    chunks = content.split("##")
    # Clean up chunks and add back the '##' header info for context
    processed_chunks = []
    ids = []
    
    for i, chunk in enumerate(chunks):
        if chunk.strip():
            # Add '##' back if it was split
            full_text = "##" + chunk if i > 0 else chunk
            processed_chunks.append(full_text.strip())
            ids.append(f"chunk_{i}")
    
    # Upsert into ChromaDB
    collection.upsert(
        documents=processed_chunks,
        ids=ids
    )
    
    print(f"Successfully indexed {len(processed_chunks)} chunks into ChromaDB at {db_path}.")

if __name__ == "__main__":
    setup_rag()
