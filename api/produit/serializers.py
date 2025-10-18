from rest_framework import serializers
from .models import Produit
from api.utilisateur.serializers import VendeurSerializer
from api.category.serializers import CategorySerializer

class ProduitSerializer(serializers.ModelSerializer):
    id_user = VendeurSerializer(read_only=True)
    id_category = CategorySerializer(read_only=True)

    class Meta:
        model = Produit
        fields = '__all__'