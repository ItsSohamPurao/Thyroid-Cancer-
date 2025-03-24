from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model_path = r"D:\ACTUAL STUDY MATERIAL\PythonCodes\ML\Thyroid Cancer\App\Models\thyroid_cancer_risk_model.pkl"

model = pickle.load(open(model_path,'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        gender = int(request.form["gender"])
        ethnicity = int(request.form["ethnicity"])
        family_history = int(request.form["family_history"])
        radiation_exposure = int(request.form["radiation_exposure"])
        iodine_deficiency = int(request.form["iodine_deficiency"])
        obesity = int(request.form["obesity"])
        diabetes = int(request.form["diabetes"])
        thyroid_cancer_risk = int(request.form["thyroid_cancer_risk"])
        continent = int(request.form["continent"])

        input_features = np.array([[gender, ethnicity, family_history, radiation_exposure,
                                    iodine_deficiency, obesity, diabetes, thyroid_cancer_risk, continent]])


        # Make prediction
        prediction = model.predict(input_features)[0]

        # Convert prediction to Yes/No
        diagnosis = "Yes" if prediction == 1 else "No"

    except Exception as e:
        diagnosis = f"Error: {str(e)}"

    return render_template("index.html", prediction=diagnosis)

if __name__ == "__main__":
    app.run(debug=True)
