from django import forms

SEX_CHOICES = [
    (1, 'Male'),
    (0, 'Female'),
]

CP_CHOICES = [
    (0, 'Typical Angina'),
    (1, 'Atypical Angina'),
    (2, 'Non-Anginal Pain'),
    (3, 'Asymptomatic'),
]

YES_NO_CHOICES = [
    (1, 'Yes'),
    (0, 'No'),
]

SLOPE_CHOICES = [
    (0, 'Upsloping'),
    (1, 'Flat'),
    (2, 'Downsloping'),
]

THAL_CHOICES = [
    (1.0, 'Fixed Defect'),
    (2.0, 'Normal'),
    (3.0, 'Reversible Defect'),
]

class MedicalForm(forms.Form):
    age = forms.IntegerField(min_value=1, max_value=120, label="Age")
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.RadioSelect, label="Sex")
    cp = forms.ChoiceField(choices=CP_CHOICES, label="Chest Pain Type")
    exang = forms.ChoiceField(choices=YES_NO_CHOICES, widget=forms.RadioSelect, label="Exercise Induced Angina")
    trestbps = forms.IntegerField(min_value=80, max_value=200, label="Resting Blood Pressure")
    thalach = forms.IntegerField(min_value=60, max_value=220, label="Maximum Heart Rate Achieved")
    chol = forms.IntegerField(min_value=100, max_value=600, label="Serum Cholesterol")
    fbs = forms.ChoiceField(choices=YES_NO_CHOICES, widget=forms.RadioSelect, label="Fasting Blood Sugar > 120 mg/dl")
    restecg = forms.IntegerField(min_value=0, max_value=2, label="Resting ECG Results")
    oldpeak = forms.FloatField(min_value=0, max_value=10, label="Oldpeak (ST Depression)")
    slope = forms.ChoiceField(choices=SLOPE_CHOICES, label="Slope of Peak Exercise ST Segment")
    ca = forms.IntegerField(min_value=0, max_value=3, label="Number of Major Vessels")
    thal = forms.ChoiceField(choices=THAL_CHOICES, label="Thalassemia")
