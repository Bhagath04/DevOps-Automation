import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_PATH = os.path.join(BASE_DIR, "knowledge_base")

documents = SimpleDirectoryReader(
    KB_PATH,
    recursive=True,
    required_exts=[".sh", ".txt", ".md"]
).load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

def query_rag(question):
    response = query_engine.query(question)
    return str(response)
