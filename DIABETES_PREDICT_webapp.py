from pathlib import Path
import pickle

import numpy as np
import streamlit as st


APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "trained_model.sav"

FEATURES = [
    ("Pregnancies", 0.0, 20.0, 0.0),
    ("Glucose", 0.0, 250.0, 120.0),
    ("Blood Pressure", 0.0, 150.0, 70.0),
    ("Skin Thickness", 0.0, 100.0, 20.0),
    ("Insulin", 0.0, 900.0, 80.0),
    ("BMI", 0.0, 80.0, 25.0),
    ("Diabetes Pedigree Function", 0.0, 3.0, 0.5),
    ("Age", 0.0, 120.0, 30.0),
]


@st.cache_resource(show_spinner=False)
def load_prediction_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model artifact not found: {MODEL_PATH.name}")
    with MODEL_PATH.open("rb") as model_file:
        return pickle.load(model_file)


def diabetes_prediction(input_data: list[float]) -> str:
    model = load_prediction_model()
    features = np.asarray(input_data, dtype=float).reshape(1, -1)
    prediction = model.predict(features)
    return "The person is diabetic" if int(prediction[0]) == 1 else "The person is not diabetic"


def main() -> None:
    st.set_page_config(page_title="Diabetes Prediction Web App", layout="centered")
    st.title("Diabetes Prediction Web App")
    st.caption("Educational ML demo using a saved diabetes prediction model.")

    st.warning(
        "This app is for portfolio and educational use only. It is not medical advice "
        "and must not be used for diagnosis or treatment decisions."
    )

    values = []
    for label, min_value, max_value, default_value in FEATURES:
        value = st.number_input(
            label,
            min_value=min_value,
            max_value=max_value,
            value=default_value,
            step=0.1,
        )
        values.append(value)

    if st.button("Predict Diabetes Risk", type="primary"):
        try:
            diagnosis = diabetes_prediction(values)
            st.success(diagnosis)
        except Exception as exc:
            st.error(f"Prediction failed: {exc}")


if __name__ == "__main__":
    main()
