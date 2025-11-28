from django.urls import path
from . import views

urlpatterns = [
    path('simuler/', views.simuler_payement, name='simuler_payement'),
    path('check/<str:id_commande>/', views.check_paiement, name='check_paiement'),
]
