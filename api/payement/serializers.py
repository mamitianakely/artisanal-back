from rest_framework import serializers
from .models import Payement
from api.utilisateur.serializers import ClientSerializer
from api.commande.serializers import CommandeSerializer

class PayementSerializer(serializers.ModelSerializer):
    id_user = ClientSerializer(read_only=True)
    id_commande = CommandeSerializer(read_only=True)

    class Meta:
        model = Payement
        fields = '__all__'