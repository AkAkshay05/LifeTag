from django import forms
from .models import LifeTagProfile

# Remove placeholder options - only keep actual valid choices
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

# Add choices for ECG results for better user experience
RESTECG_CHOICES = [
    (0, 'Normal'),
    (1, 'ST-T Wave Abnormality'),
    (2, 'Left Ventricular Hypertrophy'),
]

# Add choices for CA (Number of Major Vessels)
CA_CHOICES = [
    (0, '0 vessels'),
    (1, '1 vessel'),
    (2, '2 vessels'),
    (3, '3 vessels'),
]
BLOOD_TYPE_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]



class LifeTagForm(forms.ModelForm):
    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.RadioSelect,
        label="Sex",
        required=True
    )

    cp = forms.ChoiceField(
        choices=CP_CHOICES,
        label="Chest Pain Type",
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Select chest pain type'
        })
    )

    exang = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        label="Exercise Induced Angina",
        required=True
    )

    fbs = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        label="Fasting Blood Sugar > 120 mg/dl",
        required=True
    )

    slope = forms.ChoiceField(
        choices=SLOPE_CHOICES,
        label="Slope of Peak Exercise ST Segment",
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Select slope type'
        })
    )

    thal = forms.ChoiceField(
        choices=THAL_CHOICES,
        label="Thalassemia",
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Select thalassemia type'
        })
    )

    age = forms.IntegerField(
        min_value=1,
        max_value=120,
        label="Age",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter age (years)',
            'class': 'form-input'
        }),
        help_text="Patient's age in years."
    )

    trestbps = forms.IntegerField(
        min_value=80,
        max_value=200,
        label="Resting Blood Pressure",
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g., 120 (mm Hg)',
            'class': 'form-input'
        }),
        help_text="Measured in mm Hg (normal is around 120/80)."
    )

    thalach = forms.IntegerField(
        min_value=60,
        max_value=220,
        label="Maximum Heart Rate Achieved",
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g., 180 (bpm)',
            'class': 'form-input'
        }),
        help_text="Maximum heart rate reached during exercise."
    )

    chol = forms.IntegerField(
        min_value=100,
        max_value=600,
        label="Serum Cholesterol",
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g., 200 (mg/dl)',
            'class': 'form-input'
        }),
        help_text="Measured in mg/dl (normal is less than 200)."
    )

    # Convert to ChoiceField for better user experience
    restecg = forms.ChoiceField(
        choices=RESTECG_CHOICES,
        label="Resting ECG Results",
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Select ECG result'
        }),
        help_text="Resting electrocardiogram results"
    )

    oldpeak = forms.FloatField(
        min_value=0,
        max_value=10,
        label="Oldpeak (ST Depression)",
        widget=forms.NumberInput(attrs={
            'step': 0.1,
            'placeholder': 'e.g., 1.0',
            'class': 'form-input'
        }),
        help_text="ST depression induced by exercise relative to rest."
    )

    # Convert to ChoiceField for better user experience
    ca = forms.ChoiceField(
        choices=CA_CHOICES,
        label="Number of Major Vessels",
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Select number of vessels'
        }),
        help_text="Number of major vessels (0-3) colored by fluoroscopy."
    )

    class Meta:
        model = LifeTagProfile
        exclude = ['risk_level', 'qr_code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add empty option to select fields for better UX
        self.fields['cp'].empty_label = "Select chest pain type"
        self.fields['slope'].empty_label = "Select slope type"
        self.fields['thal'].empty_label = "Select thalassemia type"
        self.fields['restecg'].empty_label = "Select ECG result"
        self.fields['ca'].empty_label = "Select number of vessels"

        # Add CSS classes for consistent styling
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})
            elif isinstance(field.widget, forms.NumberInput):
                field.widget.attrs.update({'class': 'form-input'})
            elif isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs.update({'class': 'form-radio'})