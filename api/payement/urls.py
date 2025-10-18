from django.urls import path
from . import views

urlpatterns = [
    path('simuler/', views.simuler_payement, name='simuler_payement'),
]
