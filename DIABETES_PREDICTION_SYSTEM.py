from pathlib import Path
import pickle

import numpy as np


MODEL_PATH = Path(__file__).resolve().parent / "trained_model.sav"


def load_model():
    with MODEL_PATH.open("rb") as model_file:
        return pickle.load(model_file)


def predict_diabetes(input_data: tuple[float, ...]) -> str:
    model = load_model()
    features = np.asarray(input_data, dtype=float).reshape(1, -1)
    prediction = model.predict(features)
    return "The person is diabetic" if int(prediction[0]) == 1 else "The person is not diabetic"


if __name__ == "__main__":
    sample_input = (5, 166, 72, 19, 175, 25.8, 0.587, 51)
    print(predict_diabetes(sample_input))
