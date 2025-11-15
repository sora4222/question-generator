"""Shared state module.

This module provides a centralized location for storing and accessing
shared resources like the vector store.
"""

from typing import Optional

from langchain_chroma import Chroma


class AppState:
    """Singleton class to hold application-wide state."""

    _instance = None
    _vector_store: Optional[Chroma] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def vector_store(self) -> Optional[Chroma]:
        """Get the vector store instance."""
        return self._vector_store

    @vector_store.setter
    def vector_store(self, store: Chroma):
        """Set the vector store instance."""
        self._vector_store = store

    def get_vector_store(self) -> Chroma:
        """
        Get the vector store, raising an error if not initialized.

        Returns:
            Chroma: The vector store instance

        Raises:
            RuntimeError: If vector store has not been initialized
        """
        if self._vector_store is None:
            raise RuntimeError("Vector store has not been initialized. ")
        return self._vector_store


# Create a single instance
_app_state = AppState()


def get_app_state() -> AppState:
    """Get the application state singleton."""
    return _app_state


def set_vector_store(vector_store: Chroma):
    """Set the vector store in the application state."""
    _app_state.vector_store = vector_store


def get_vector_store() -> Chroma:
    """Get the vector store from the application state."""
    return _app_state.get_vector_store()
