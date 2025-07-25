from django.shortcuts import render
from .forms import MedicalForm
from .predictor import predict_risk

def medical_form_view(request):
    if request.method == 'POST':
        form = MedicalForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            input_data = {
                'age': cleaned['age'],
                'sex': int(cleaned['sex']),
                'cp': int(cleaned['cp']),
                'trestbps': cleaned['trestbps'],
                'chol': cleaned['chol'],
                'fbs': int(cleaned['fbs']),
                'restecg': cleaned['restecg'],
                'thalach': cleaned['thalach'],
                'exang': int(cleaned['exang']),
                'oldpeak': cleaned['oldpeak'],
                'slope': int(cleaned['slope']),
                'ca': cleaned['ca'],
                'thal': float(cleaned['thal']),
            }

            risk = predict_risk(input_data)

            return render(request, 'heart/result.html', {
                'risk_level': risk,
                'data': input_data,
            })
        else:
            print("Form errors:", form.errors)  # Add this to debug why form invalid
    else:
        form = MedicalForm()

    return render(request, 'heart/medical_form.html', {'form': form})
