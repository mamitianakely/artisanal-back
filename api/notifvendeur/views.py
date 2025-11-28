# api/notifvendeur/views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import NotifVendeur
from .serializers import NotifVendeurSerializer

class NotifVendeurViewSet(viewsets.ModelViewSet):
    serializer_class = NotifVendeurSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return NotifVendeur.objects.filter(user=user).order_by('-date_creation')

    # ✅ Marquer une seule notification comme lue
    @action(detail=True, methods=['patch'])
    def mark_as_read(self, request, pk=None):
        notifVendeur = self.get_object()
        notifVendeur.is_read = True
        notifVendeur.save()
        return Response({"message": "Notification marquée comme lue"}, status=status.HTTP_200_OK)

    # ✅ Marquer toutes les notifications comme lues
    @action(detail=False, methods=['patch'])
    def mark_all_as_read(self, request):
        notifVendeurs = NotifVendeur.objects.filter(user=request.user, is_read=False)
        count = notifVendeurs.update(is_read=True)
        return Response(
            {"message": f"{count} notification(s) marquée(s) comme lue(s)."},
            status=status.HTTP_200_OK
        )
