from rest_framework import serializers
from .models import Commande
from api.utilisateur.serializers import ClientSerializer

class CommandeSerializer(serializers.ModelSerializer):
    id_user = ClientSerializer(read_only=True)

    class Meta:
        model = Commande
        fields = '__all__'