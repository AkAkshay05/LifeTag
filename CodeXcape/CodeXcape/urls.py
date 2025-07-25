from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from xcape.views import generate_qr_view, view_details  # adjust app name
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', generate_qr_view, name='generate_qr'),
    path('view/<int:id>/', view_details, name='view_details'),
    path('heart/', include('heart.urls')),
    path('lifetag/', include('lifetag.urls')),
    path('', views.welcome_page, name='welcome'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
