from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import LifeTagForm
from .models import LifeTagProfile
from .utils import predict_risk, generate_qr

from .utils import generate_qr



def lifetag_form(request):
    if request.method == 'POST':
        form = LifeTagForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)

            # Predict risk from form data
            profile.risk_level = predict_risk(form.cleaned_data)

            # Generate QR code
            qr_content = generate_qr(profile)

            # Save QR image
            profile.qr_code.save(qr_content.name, qr_content, save=False)
            profile.save()

            return redirect('lifetag_result', pk=profile.pk)
    else:
        form = LifeTagForm()

    return render(request, 'lifetag/form.html', {'form': form})



def welcome_page(request):
    return render(request, 'lifetag/welcome.html')

def lifetag_result(request, pk):
    profile = get_object_or_404(LifeTagProfile, pk=pk)
    return render(request, 'lifetag/result.html', {'profile': profile})

def lifetag_qr_view(request, pk):
    profile = get_object_or_404(LifeTagProfile, pk=pk)
    return render(request, 'lifetag/view.html', {'profile': profile})
from django.shortcuts import render

# Create your views here.
