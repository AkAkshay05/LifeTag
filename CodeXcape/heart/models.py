from django.db import models

class Patient(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()  # 1 = male, 0 = female
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.BooleanField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()
    risk_level = models.CharField(max_length=20, blank=True, null=True)  # "High Risk" or "Low Risk"
from django.db import models

# Create your models here.
