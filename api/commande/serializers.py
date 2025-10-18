from rest_framework import serializers
from .models import Commande
from api.utilisateur.serializers import ClientSerializer
from api.ligneCommande.serializers import LigneCommandeSerializer

class CommandeSerializer(serializers.ModelSerializer):
    id_user = ClientSerializer(read_only=True)

    class Meta:
        model = Commande
        fields = '__all__'

    def to_representation(self, instance):
        from api.ligneCommande.serializers import LigneCommandeSerializer
        rep = super().to_representation(instance)
        rep['ligneCommandes'] = LigneCommandeSerializer(instance.ligneCommandes.all(), many=True).data
        return rep

