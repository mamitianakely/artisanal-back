# api/produit/views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Produit
from .serializers import ProduitSerializer
from api.notifvendeur.models import NotifVendeur

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all().order_by('-datePublication')
    serializer_class = ProduitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(id_user=self.request.user)

    # Surcharge de update pour gérer le PATCH du statut
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        old_statut = instance.statut  # Sauvegarde de l'ancien statut

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Création automatique de la notification si le statut change
        new_statut = serializer.instance.statut
        if old_statut != new_statut:
            if new_statut == "validee":
                message_text = f"Votre produit '{instance.nomProduit}' a été validé ✅"
                notif_type = "validation"
            elif new_statut == "refusee":
                message_text = f"Votre produit '{instance.nomProduit}' a été refusé ❌"
                notif_type = "refus"
            else:
                message_text = None
                notif_type = None

            if message_text:
                NotifVendeur.objects.create(
                    user=instance.id_user,  # Utilisateur qui a publié le produit
                    produit=instance,
                    message=message_text,
                    type=notif_type
                )

        return Response(serializer.data)
