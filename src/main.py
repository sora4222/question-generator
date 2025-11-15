from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from langchain.messages import HumanMessage
from src.chroma.client import setup_chroma_collection
from src.models.agent import create_or_get_agent
from src.state import set_vector_store


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Sets up the LangChain agent with ChromaDB and Ollama."""
    # Set up ChromaDB collection and vector store
    vector_store = await setup_chroma_collection(
        collection_name="notion",
        embedding_model="embeddinggemma:300m",
        ollama_url="http://localhost:11434",
        update_collection=True,
    )

    # Store vector store in shared state for access by tools
    set_vector_store(vector_store)

    # Create agent with configurable model
    create_or_get_agent(
        model_name="llama3.2:3b",
        ollama_url="http://localhost:11434",
    )

    yield

    # Cleanup could be added here if needed


app = FastAPI(lifespan=lifespan)


@app.get("/question/generate")
def generate_question():
    """
    Generates a question using LangChain.
    """
    agent = create_or_get_agent()
    response = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="My partner is named Phu. I can't remember her brothers name, can you help?"
                )
            ]
        }
    )
    return {"question": response}


@app.get("/healthz")
def healthz():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
