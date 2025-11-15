from langchain.tools import tool
from src.state import get_vector_store


@tool
def information_retrieval(query: str):
    """Obtains information relevant to the query"""
    vector_store = get_vector_store()
    docs = vector_store.similarity_search(query, k=2)
    return "\n\n".join([doc.page_content for doc in docs])
