from fastapi import APIRouter, HTTPException
from models.score import ScoreRequest, ScoreResponse
from ai.credit_gnn import CreditGNN, build_mock_graph
from utils.helpers import validate_consent

router = APIRouter()

@router.post("/score", response_model=ScoreResponse)
async def get_credit_score(request: ScoreRequest):
    if not validate_consent(request.consent_token):
        raise HTTPException(status_code=401, detail="Invalid consent token")

    # Build graph from features
    graph = build_mock_graph(request.features)
    
    # Model inference
    model = CreditGNN()
    score = model(graph).item()
    
    credit_score = round(300 + score * 600, 1)
    pd = round((1 - score) * 100, 2)  # Probability of Default
    
    risk_level = "Low" if credit_score >= 750 else "Medium" if credit_score >= 550 else "High"
    
    return ScoreResponse(
        credit_score=credit_score,
        risk_level=risk_level,
        probability_of_default=pd,
        explanation={
            "top_factors": [
                {"factor": "UPI Transaction Consistency", "impact": "+28%"},
                {"factor": "GST Filing Regularity", "impact": "+22%"},
                {"factor": "Utility Payment History", "impact": "+18%"}
            ],
            "recommendation": "Strong cash flow patterns detected."
        },
        graph_data={
            "nodes": [
                {"id": "user", "label": "Applicant", "score": credit_score},
                {"id": "m1", "label": "Merchant A", "type": "transaction"}
            ],
            "edges": [{"from": "user", "to": "m1"}]
        },
        message="Score generated using GNN on alternative data."
    )
