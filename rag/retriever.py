from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma(
    persist_directory="rag/vector_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


def retrieve_math_rules(query):

    docs = retriever.invoke(query)

    if not docs:
        return {
            "rules": [],
            "retrieval_failed": True
        }

    return {
        "rules": [doc.page_content for doc in docs],
        "retrieval_failed": False
    }