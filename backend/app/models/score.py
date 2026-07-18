from pydantic import BaseModel
from typing import Dict, List, Any

class ScoreRequest(BaseModel):
    consent_token: str
    features: Dict[str, float]

class ScoreResponse(BaseModel):
    credit_score: float
    risk_level: str
    probability_of_default: float
    explanation: Dict[str, Any]
    graph_data: Dict[str, Any]
    message: str
