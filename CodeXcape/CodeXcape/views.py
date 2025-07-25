from django.shortcuts import render
from xcape.models import Xcape
def home_view(request):
    name= "Welcome to"

    obj = Xcape.objects.get(id=1)
    context= {
        'name' : name,
        'obj' : obj,
    }

    return render(request, 'home.html', context)


def welcome_page(request):
    return render(request, 'lifetag/welcome.html')