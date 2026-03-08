from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

print("Loading documents...")

loader = DirectoryLoader(
    "rag/docs",
    glob="**/*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

print(f"Loaded {len(documents)} documents")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

vectorstore = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="rag/vector_db"
)

vectorstore.persist()

print("Vector store created successfully")