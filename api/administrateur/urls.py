# api/administrateur/urls.py
from django.urls import path
from . import views  # ✅ import du fichier views du même dossier

urlpatterns = [
    path('transactions-total/', views.total_transactions, name='total-transactions'),
    path('produits-total/', views.total_produits, name='total-produits'),
    path('transactions-recentes/', views.transactions_recentes, name='transactions-recentes'),
    path('repartition-payements/', views.repartition_payements, name='repartition-payements'),
    path('liste-paiements/', views.liste_paiements, name='liste_paiements'),

]
