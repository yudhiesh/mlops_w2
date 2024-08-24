from pydantic import BaseModel
from src.constants import SentimentLabel

class SimpleModelRequest(BaseModel):
    review: str

class SimpleModelResponse(BaseModel):
    probability: float
    label: SentimentLabel