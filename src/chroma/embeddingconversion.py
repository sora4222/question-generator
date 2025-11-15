from langchain_core.embeddings import Embeddings


class DefChromaEF(Embeddings):
    """
    Used for wrapping the Chroma embedding function.
    For compatibility with LangChain.
    """

    def __init__(self, ef):
        self.ef = ef

    def embed_documents(self, texts):
        return self.ef(texts)

    def embed_query(self, query):
        return self.ef([query])[0]
