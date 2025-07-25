import joblib
import numpy as np
import os

# Load model once when module loads
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'risk_predictor.pkl')
model = joblib.load(MODEL_PATH)

def predict_risk(data):
    """
    data: dict containing features as keys and values from patient form,
    e.g. {'age': 50, 'sex': 1, ...}
    """
    features = np.array([
        data['age'],
        data['sex'],
        data['cp'],
        data['trestbps'],
        data['chol'],
        data['fbs'],
        data['restecg'],
        data['thalach'],
        data['exang'],
        data['oldpeak'],
        data['slope'],
        data['ca'],
        data['thal'],
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    return "High Risk" if prediction == 1 else "Low Risk"
