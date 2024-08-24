import wandb
import numpy as np
import onnxruntime as rt
from src.constants import WANDB_MODEL_REGISTRY_MODEL_NAME
from src.data_models import SimpleModelRawResults

def load_model() -> rt.InferenceSession:
    run = wandb.init()
    downloaded_model_path = run.use_model(name=WANDB_MODEL_REGISTRY_MODEL_NAME)
    return rt.InferenceSession(downloaded_model_path, providers=['CPUExecutionProvider'])

def predict(review: str, session: rt.InferenceSession) -> SimpleModelRawResults:
    input_name = session.get_inputs()[0].name
    _, probas = session.run(None, {input_name: np.array([[review]])})
    return SimpleModelRawResults(**probas[0])