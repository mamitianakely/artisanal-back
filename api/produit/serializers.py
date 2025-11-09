from rest_framework import serializers
from .models import Produit
from api.utilisateur.serializers import UtilisateurSerializer
from api.category.serializers import CategorySerializer
from api.category.views import Category

class ProduitSerializer(serializers.ModelSerializer):
    id_user = UtilisateurSerializer(read_only=True)
    id_category = CategorySerializer(read_only=True)
    id_category_id = serializers.PrimaryKeyRelatedField(
        queryset= Category.objects.all(),
        source='id_category',
        write_only=True
    )

    class Meta:
        model = Produit
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},  # Permet l'image optionnelle
        }