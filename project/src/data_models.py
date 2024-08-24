from pydantic import BaseModel, Field, ConfigDict
from src.constants import SentimentLabel

class Sentiment(BaseModel):
    score: float = Field(description="Probability score of the sentiment class", ge=0, le=1)

class SimpleModelRawResults(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    results = dict[SentimentLabel, Sentiment]

class SimpleModelRequest(BaseModel):
    review: str

class SimpleModelResponse(BaseModel):
    probability: float
    label: SentimentLabel