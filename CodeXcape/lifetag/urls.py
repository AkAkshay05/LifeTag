from django.urls import path
from . import views

urlpatterns = [
    path('', views.lifetag_form, name='lifetag_form'),
    path('result/<int:pk>/', views.lifetag_result, name='lifetag_result'),
    path('view/<int:pk>/', views.lifetag_qr_view, name='lifetag_qr_view'),
]
