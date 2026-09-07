from fastapi import FastAPI

from .risk_engine import evaluate_assessment
from .schemas import AssessmentInput, AssessmentResult


app = FastAPI(
    title="Cloud Security Architecture Review API",
    version="0.1.0",
    description="Evaluates cloud architecture security questionnaires and returns risk-ranked findings.",
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/api/v1/assessments/evaluate", response_model=AssessmentResult)
def evaluate(payload: AssessmentInput) -> AssessmentResult:
    return evaluate_assessment(payload)
