from rest_framework import serializers
from api.payement.models import Payement

class PayementSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source="id_user.nomClient", read_only=True)
    produit = serializers.CharField(source="id_commande.produit.nomProduit", read_only=True)

    class Meta:
        model = Payement
        fields = ["id_payement", "montant", "typePayement", "datePayement", "client", "produit"]
