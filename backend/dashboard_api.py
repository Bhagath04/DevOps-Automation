from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Metric(BaseModel):
    name: str
    value: float

# Sample endpoint to get dashboard metrics
@app.get("/metrics", response_model=list[Metric])
def get_metrics():
    metrics = [
        Metric(name="CPU Usage", value=75.5),
        Metric(name="Memory Usage", value=65.2),
    ]
    return metrics

# Sample endpoint to get dashboard data
@app.get("/dashboard")
def get_dashboard():
    return {"status": "success", "message": "Dashboard data loaded successfully."}