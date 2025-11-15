"""Agent management module.

This module provides functions to create and manage LangChain agents
with configurable models and tools.
"""

from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from src.models.information_retrieval import information_retrieval


class AgentManager:
    """Manages LangChain agent instances."""

    _instance = None
    _agent = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def agent(self):
        """Get the current agent instance."""
        return self._agent

    @agent.setter
    def agent(self, agent_instance):
        """Set the agent instance."""
        self._agent = agent_instance


def create_or_get_agent(
    model_name: str = "gemma:7b",
    ollama_url: str = "http://localhost:11434",
    recreate: bool = False,
):
    """
    Creates or retrieves a LangChain agent with the specified configuration.

    Args:
        model_name: Name of the Ollama model to use
        ollama_url: URL of the Ollama server
        recreate: If True, forces recreation of the agent even if one exists

    Returns:
        The LangChain agent instance

    Raises:
        ValueError: If vector_store is not provided when creating a new agent
    """
    manager = AgentManager()

    # Return existing agent if available and not forcing recreation
    if manager.agent is not None and not recreate:
        return manager.agent

    # Create chat model
    chat_model = ChatOllama(model=model_name, base_url=ollama_url)

    # Create agent with tools
    agent = create_agent(
        model=chat_model,
        tools=[information_retrieval],
    )

    # Store the agent
    manager.agent = agent

    return agent


def get_agent():
    """
    Get the current agent instance.

    Returns:
        The current agent instance

    Raises:
        RuntimeError: If no agent has been created yet
    """
    manager = AgentManager()
    if manager.agent is None:
        raise RuntimeError("No agent has been created. Call create_or_get_agent first.")
    return manager.agent
