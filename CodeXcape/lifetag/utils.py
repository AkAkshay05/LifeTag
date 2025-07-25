import joblib
import os
from io import BytesIO
import qrcode
from django.core.files.base import ContentFile

# Build absolute path to your model file safely
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'heart', 'risk_predictor.pkl')


def predict_risk(data):
    # Load the trained model
    model = joblib.load(MODEL_PATH)

    # Extract features from data dict in proper order
    features = [
        data['age'], data['sex'], data['cp'], data['trestbps'], data['chol'],
        data['fbs'], data['restecg'], data['thalach'], data['exang'],
        data['oldpeak'], data['slope'], data['ca'], data['thal']
    ]

    # Run prediction and interpret result
    prediction = model.predict([features])[0]
    return 'High' if prediction == 1 else 'Low'


def generate_qr(profile):
    # Construct the URL you want to encode in the QR code
    url = f"http://yourdomain.com/lifetag/view/{profile.id}/"

    # Generate QR code image
    qr = qrcode.make(url)

    # Save QR code image to an in-memory bytes buffer
    buffer = BytesIO()
    qr.save(buffer, format='PNG')  # Explicit format recommended

    # Create a Django ContentFile from the buffer's contents
    filename = f"qr_{profile.id}.png"
    return ContentFile(buffer.getvalue(), name=filename)
