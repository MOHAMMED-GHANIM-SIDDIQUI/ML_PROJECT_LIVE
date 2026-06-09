from pathlib import Path


APP_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = APP_DIR / "models" / "trained_model.sav"

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
