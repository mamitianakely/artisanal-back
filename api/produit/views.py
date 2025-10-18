from rest_framework import viewsets
from .models import Produit
from .serializers import ProduitSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all().order_by('-datePublication')
    serializer_class = ProduitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(id_user=self.request.user)

    # Pour tester sans authentification
    #def perform_create(self, serializer):
        #serializer.save()