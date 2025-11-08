# api/notifvendeur/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import NotifVendeur
from .serializers import NotifVendeurSerializer

class NotifVendeurViewSet(viewsets.ModelViewSet):
    serializer_class = NotifVendeurSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 🔹 Retourne seulement les notifications de l'utilisateur connecté
        user = self.request.user
        return NotifVendeur.objects.filter(user=user).order_by('-date_creation')
