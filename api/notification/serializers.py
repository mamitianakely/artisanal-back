from rest_framework import serializers
from .models import Notification
from api.commande.models import Commande  # Import du modèle Commande

# Sérialiseur minimal pour la commande
class CommandeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ['id_commande', 'total', 'statut']  # Ajuste selon tes besoins

# Sérialiseur Notification avec jointure commande
class NotificationSerializer(serializers.ModelSerializer):
    commande = serializers.SerializerMethodField()  # champ calculé

    class Meta:
        model = Notification
        fields = ['id_notification', 'message', 'is_read', 'date_creation', 'commande']

    def get_commande(self, obj):
        if obj.commande_id:  # ← utiliser le bon champ ici
            try:
                commande = Commande.objects.get(id_commande=obj.commande_id)
                return CommandeMiniSerializer(commande).data
            except Commande.DoesNotExist:
                return None
        return None
