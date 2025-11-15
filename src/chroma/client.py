"""ChromaDB client and collection initialization."""

import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction
from langchain_chroma import Chroma

from src.chroma.embeddingconversion import DefChromaEF
from src.chroma.notion import update_notion_collection


class ChromaClientSingleton:
    """Singleton to manage a single ChromaDB client instance."""

    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def client(self):
        if self._client is None:
            self._client = chromadb.Client()
        return self._client


def get_chroma_client() -> chromadb.ClientAPI:
    """
    Gets or creates a ChromaDB client.

    Returns:
        chromadb.ClientAPI: The ChromaDB client instance.
    """
    singleton = ChromaClientSingleton()
    return singleton.client


async def setup_chroma_collection(
    collection_name: str = "notion",
    embedding_model: str = "embeddinggemma:300m",
    ollama_url: str = "http://localhost:11434",
    update_collection: bool = True,
) -> Chroma:
    """
    Sets up ChromaDB collection and optionally updates it with Notion data.

    Args:
        collection_name: Name of the ChromaDB collection
        embedding_model: Name of the Ollama embedding model to use
        ollama_url: URL of the Ollama server
        update_collection: Whether to update the collection with Notion data

    Returns:
        Chroma: LangChain Chroma vector store instance
    """
    # Get or create client
    chroma_client = get_chroma_client()

    # Set up embedding function
    embedding_function = OllamaEmbeddingFunction(
        model_name=embedding_model, url=ollama_url
    )

    # Get or create collection
    chroma_collection = chroma_client.get_or_create_collection(
        name=collection_name, embedding_function=embedding_function
    )

    # Update collection with Notion data if requested
    if update_collection:
        await update_notion_collection(chroma_collection)

    # Create LangChain Chroma vector store
    vector_store = Chroma(
        collection_name=collection_name,
        embedding_function=DefChromaEF(embedding_function),
        client=chroma_client,
    )

    return vector_store
