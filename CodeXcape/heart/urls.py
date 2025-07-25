from django.urls import path

from . import views
from .views import medical_form_view

urlpatterns = [
    path('', medical_form_view, name='medical_form'),
    path('assessment/', views.medical_form_view, name='medical_form'),
]
