from rest_framework.routers import DefaultRouter
from .views import LoginView, UtilisateurViewSet, ClientViewSet, VendeurViewSet
from django.urls import path


routeur = DefaultRouter()
routeur.register(r'', UtilisateurViewSet, basename='utilisateur')
routeur.register(r'clients', ClientViewSet, basename='client')
routeur.register(r'vendeurs', VendeurViewSet, basename='vendeur')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]

# On ajoute aussi les routes du routeur
urlpatterns += routeur.urls
