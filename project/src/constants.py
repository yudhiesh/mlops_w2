import os
from enum import Enum


class SentimentLabel(Enum):
    NEGATIVE = (0, "Negative")
    NEUTRAL = (1, "Neutral")
    POSITIVE = (2, "Positive")


WANDB_MODEL_REGISTRY_MODEL_NAME = (
    "yudhiesh/model-registry/Drugs Review MLOps Uplimit:v1"
)

WANDB_API_KEY = os.getenv("WANDB_API_KEY")
