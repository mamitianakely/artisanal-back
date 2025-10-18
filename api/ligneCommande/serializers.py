from rest_framework import serializers
from .models import LigneCommande
from api.produit.serializers import ProduitSerializer
from api.commande.serializers import CommandeSerializer

class LigneCommandeSerializer(serializers.ModelSerializer):
    id_produit = ProduitSerializer(read_only=True)
    id_commande = CommandeSerializer(read_only=True)

    class Meta:
        model = LigneCommande
        fields = '__all__'