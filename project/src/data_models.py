from pydantic import BaseModel

from src.constants import SentimentLabel


class SentimentScore(BaseModel):
    score: float


class SimpleModelRequest(BaseModel):
    review: str


class SimpleModelResponse(BaseModel):
    probability: float
    label: SentimentLabel
