import pickle

model_path = r"d:\ACTUAL STUDY MATERIAL\PythonCodes\ML\Thyroid Cancer\Models\thyroid_cancer_risk_model.pkl"

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully:", type(model))
except Exception as e:
    print("Error loading model:", e)
