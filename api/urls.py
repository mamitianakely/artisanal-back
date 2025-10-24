from django.urls import path, include


urlpatterns = [
    path('category/', include('api.category.urls')),
    path('utilisateur/', include('api.utilisateur.urls')),
    path('produit/', include('api.produit.urls')),
    path('commande/', include('api.commande.urls')),
    path('lignecommande/', include('api.ligneCommande.urls')),
    path('payement/', include('api.payement.urls')),
    path('promotion/', include('api.promotion.urls')),
    path('notification/', include('api.notification.urls')),
    path('administrateur/', include('api.administrateur.urls')),
]