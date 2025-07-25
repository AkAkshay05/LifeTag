from django import forms
from .models import Xcape

class XcapeForm(forms.ModelForm):
    class Meta:
        model = Xcape
        fields = [
            'name',
            'guardian_phone',
            'address',
            'blood_type',
            'allergies',
            'description',
        ]
