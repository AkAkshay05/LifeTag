from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import XcapeForm
from .models import Xcape

def generate_qr_view(request):
    form = XcapeForm()
    if request.method == 'POST':
        form = XcapeForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('view_details', id=obj.id)

    return render(request, 'generate.html', {'form': form})

def view_details(request, id):
    obj = get_object_or_404(Xcape, id=id)
    return render(request, 'details.html', {'obj': obj})
