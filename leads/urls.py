from django.urls import path
from .views import capture_lead

urlpatterns = [
    path('', capture_lead, name='capture_lead'),
]