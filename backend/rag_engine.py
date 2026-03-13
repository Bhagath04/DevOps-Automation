from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("knowledge_base").load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

def query_rag(question: str):
    response = query_engine.query(question)
    return str(response)
