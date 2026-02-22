import chromadb
from chromadb.utils import embedding_functions
import os

def query_offer_mart(user_query, n_results=2):
    """
    Retrieves the most relevant policy/product chunks from the Offer Mart vector database.
    """
    db_path = os.path.join(os.getcwd(), "chroma_db")
    client = chromadb.PersistentClient(path=db_path)
    
    # Use the same default embedding function as during setup
    default_ef = embedding_functions.DefaultEmbeddingFunction()
    
    collection = client.get_collection(
        name="offer_mart",
        embedding_function=default_ef
    )
    
    results = collection.query(
        query_texts=[user_query],
        n_results=n_results
    )
    
    # Flatten the results for the agent to consumption
    documents = results['documents'][0]
    return "\n\n".join(documents)

if __name__ == "__main__":
    # Test the tool
    test_query = "What are the interest rates for personal loans?"
    context = query_offer_mart(test_query)
    print(f"Query: {test_query}\n")
    print(f"Retrieved Context:\n{context}")
