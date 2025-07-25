# lifetag/models.py
from django.db import models


class LifeTagProfile(models.Model):
    # Personal / Emergency Info
    name = models.CharField(max_length=200)
    guardian_phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    blood_type = models.CharField(max_length=5)
    allergies = models.TextField(blank=True)
    description = models.TextField(blank=True)

    # Heart Prediction Fields
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.FloatField()

    # Prediction Result
    risk_level = models.CharField(max_length=10, blank=True)

    # QR Code
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return self.name
