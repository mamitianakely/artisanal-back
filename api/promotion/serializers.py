from rest_framework import serializers
from .models import Promotion
from api.produit.models import Produit  # Assure-toi d'importer le modèle Produit
from api.produit.serializers import ProduitSerializer

class PromotionSerializer(serializers.ModelSerializer):
    id_produit = ProduitSerializer(read_only=True)  # affichage du produit complet
    id_produit_id = serializers.PrimaryKeyRelatedField(
        queryset=Produit.objects.all(),  # ✅ utiliser les produits
        write_only=True,
        source='id_produit'
    )

    class Meta:
        model = Promotion
        fields = ['id_prom', 'id_produit', 'id_produit_id', 'prixAvant', 'prixApres', 'date_debut', 'date_fin']
