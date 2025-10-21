from rest_framework import serializers
from .models import Commande
from api.ligneCommande.models import LigneCommande
from api.ligneCommande.serializers import LigneCommandeSerializer
from rest_framework.exceptions import PermissionDenied

class CommandeSerializer(serializers.ModelSerializer):
    ligneCommandes = LigneCommandeSerializer(many=True, read_only=True)
    id_user = serializers.StringRelatedField(read_only=True)
    statut = serializers.CharField(read_only=True)
    total = serializers.FloatField(read_only=True)

    class Meta:
        model = Commande
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        if user.role != 'client':
            raise PermissionDenied("Seul un client peut créer une commande.")

        panier = request.data.get('panier', [])
        if not panier:
            raise serializers.ValidationError("Le panier est vide ou non fourni.")

        # Créer la commande avec total provisoire à 0
        commande = Commande.objects.create(
            id_user=user,
            statut='En attente',
            total=0
        )

        total = 0
        for item in panier:
            quantite = int(item.get('quantite', 0))
            prix_unitaire = float(item.get('prixUnitaire', 0))
            sous_total = quantite * prix_unitaire
            total += sous_total

            # Créer la ligne de commande
            LigneCommande.objects.create(
                id_produit_id=item['id_produit'],
                id_commande=commande,
                quantiteCommande=quantite,
                sousTotal=sous_total
            )

        commande.total = total
        commande.save()

        return commande
