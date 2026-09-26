from fastapi import FastAPI

from app.api.employee import router as employee_router


app = FastAPI(
    title="Worklynk AI",
    description="AI-Powered Employee Services & HR Workflow Orchestration Platform",
    version="0.1.0"
)


app.include_router(employee_router)


@app.get("/")
def root():
    return {
        "application": "Worklynk AI",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }