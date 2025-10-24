from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Commande
from .serializers import CommandeSerializer
from api.notification.models import Notification

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        statut = self.request.query_params.get('statut')

        # 🔹 Le vendeur voit toutes les commandes
        if user.role == 'vendeur':
            queryset = Commande.objects.all().order_by('-dateCommande')

        # 🔹 Le client voit seulement ses commandes
        elif user.role == 'client':
            queryset = Commande.objects.filter(id_user=user).order_by('-dateCommande')

        else:
            queryset = Commande.objects.none()

        # 🔹 Filtrer par statut si fourni
        if statut:
            queryset = queryset.filter(statut=statut)

        return queryset

    def perform_create(self, serializer):
        serializer.save()

    # 🟩 Action personnalisée pour valider une commande
    @action(detail=True, methods=['patch'], url_path='valider')
    def valider_commande(self, request, pk=None):
        user = request.user
        if user.role != 'vendeur':
            return Response({"detail": "Action réservée au vendeur."}, status=status.HTTP_403_FORBIDDEN)

        commande = self.get_object()
        commande.statut = 'Validée'
        commande.save()

        # 🟡 AJOUT : Créer une notification pour le client
        Notification.objects.create(
            user=commande.id_user,
            commande=commande,
            message="Votre commande a été validée. Veuillez procéder au paiement pour obtenir la marchandise.",
            type="validation"
        )

        return Response({"message": "Commande validée avec succès."}, status=status.HTTP_200_OK)

    # 🟥 Action personnalisée pour refuser une commande
    @action(detail=True, methods=['patch'], url_path='refuser')
    def refuser_commande(self, request, pk=None):
        user = request.user
        if user.role != 'vendeur':
            return Response({"detail": "Action réservée au vendeur."}, status=status.HTTP_403_FORBIDDEN)

        commande = self.get_object()
        commande.statut = 'Refusée'
        commande.save()

        # 🟡 AJOUT : Créer une notification pour le client
        Notification.objects.create(
            user=commande.id_user,
            commande=commande,
            message="Désolé, votre commande a été refusée.",
            type="refus"
        )


        return Response({"message": "Commande refusée avec succès."}, status=status.HTTP_200_OK)
