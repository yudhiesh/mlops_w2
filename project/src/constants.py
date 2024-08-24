from enum import IntEnum

class SentimentLabel(IntEnum):
    NEGATIVE = 0
    NEUTRAL = 1
    POSITIVE = 2

WANDB_MODEL_REGISTRY_MODEL_NAME = "yudhiesh/model-registry/Drugs Review MLOps Uplimit:v1"