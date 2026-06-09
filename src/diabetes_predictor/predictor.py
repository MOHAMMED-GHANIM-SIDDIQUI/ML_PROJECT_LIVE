import pickle
from collections.abc import Sequence

import numpy as np

from .config import MODEL_PATH


def validate_features(input_data: Sequence[float]) -> None:
    if len(input_data) != 8:
        raise ValueError("Expected exactly 8 diabetes model input features.")
    for value in input_data:
        if not isinstance(value, (int, float)):
            raise TypeError("All diabetes model input features must be numeric.")


def load_prediction_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model artifact not found: {MODEL_PATH}")
    with MODEL_PATH.open("rb") as model_file:
        return pickle.load(model_file)


def format_prediction(prediction_value: int) -> str:
    return "The person is diabetic" if int(prediction_value) == 1 else "The person is not diabetic"


def predict_diabetes(input_data: Sequence[float], model=None) -> str:
    validate_features(input_data)
    loaded_model = model or load_prediction_model()
    features = np.asarray(input_data, dtype=float).reshape(1, -1)
    prediction = loaded_model.predict(features)
    return format_prediction(int(prediction[0]))
