from rest_framework import serializers
from .models import LigneCommande
from api.produit.serializers import ProduitSerializer

class LigneCommandeSerializer(serializers.ModelSerializer):
    id_produit = ProduitSerializer(read_only=True)
    id_commande = serializers.PrimaryKeyRelatedField(read_only=True)  # <-- juste l'id

    class Meta:
        model = LigneCommande
        fields = '__all__'
