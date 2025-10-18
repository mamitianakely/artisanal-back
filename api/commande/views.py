from rest_framework import viewsets
from .models import Commande
from .serializers import CommandeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all().order_by('-dateCommande')
    serializer_class = CommandeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(id_user=self.request.user.client)

