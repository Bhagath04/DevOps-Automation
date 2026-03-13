# DevSecOps AI Assistant

AI powered RAG chatbot designed to help DevOps engineers automate tasks.

Features:
- Infrastructure automation scripts (AWS/Azure)
- CI/CD pipeline templates
- Docker build templates
- GitHub repo automation
- MuleSoft and TIBCO pipelines
- JFrog Artifactory integration
- Security scanning scripts

Architecture:
Frontend: Streamlit
Backend: FastAPI
RAG Engine: LlamaIndex
Vector DB: ChromaDB

Run Backend:
uvicorn backend.main:app --reload

Run UI:
streamlit run frontend/chat_ui.py
