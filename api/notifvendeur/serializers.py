# api/notifvendeur/serializers.py
from rest_framework import serializers
from .models import NotifVendeur
from api.produit.models import Produit

class ProduitMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id_produit', 'nomProduit', 'prixUnitaire']

class NotifVendeurSerializer(serializers.ModelSerializer):
    produit = ProduitMiniSerializer(read_only=True)  # jointure produit

    class Meta:
        model = NotifVendeur
        fields = ['id_notif', 'message', 'is_read', 'date_creation', 'produit', 'type']
