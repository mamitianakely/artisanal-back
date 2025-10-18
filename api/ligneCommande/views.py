from rest_framework import viewsets
from .models import LigneCommande
from .serializers import LigneCommandeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LigneCommandeViewSet(viewsets.ModelViewSet):
    queryset = LigneCommande.objects.all()
    serializer_class = LigneCommandeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    #def perform_create(self, serializer):
        #serializer.save(id_produit=self.request.user.produit)
        #serializer.save(id_commande=self.request.user.commande)
