import streamlit as st

from .config import FEATURES
from .predictor import load_prediction_model, predict_diabetes


@st.cache_resource(show_spinner=False)
def cached_model():
    return load_prediction_model()


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
            diagnosis = predict_diabetes(values, model=cached_model())
            st.success(diagnosis)
        except Exception as exc:
            st.error(f"Prediction failed: {exc}")
