from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Promotion
from .serializers import PromotionSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all().order_by('-date_debut')
    serializer_class = PromotionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Générer l'id_prom automatiquement
        last_promotion = Promotion.objects.order_by('id_prom').last()
        if not last_promotion:
            new_id = "PROM001"
        else:
            prom_num = int(last_promotion.id_prom.replace("PROM", ""))
            new_id = f"PROM{prom_num + 1:03d}"
        serializer.save(id_prom=new_id)
