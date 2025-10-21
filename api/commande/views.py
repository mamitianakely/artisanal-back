from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Commande
from .serializers import CommandeSerializer

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all().order_by('-dateCommande')
    serializer_class = CommandeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
