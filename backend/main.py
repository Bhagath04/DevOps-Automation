from fastapi import FastAPI
from rag_engine import query_rag

app = FastAPI(title="DevSecOps AI Assistant")

@app.get("/")
def home():
    return {"message": "DevSecOps AI Assistant Running"}

@app.post("/ask")
def ask(question: str):
    answer = query_rag(question)
    return {
        "question": question,
        "answer": answer
    }
