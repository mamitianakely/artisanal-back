from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Liste seulement les notifications du user connecté
        return Notification.objects.filter(user=self.request.user).order_by('-date_creation')

    # ✅ Marquer une notification comme lue
    @action(detail=True, methods=['patch'])
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({"message": "Notification marquée comme lue"}, status=status.HTTP_200_OK)

    # ✅ Tout marquer comme lu
    @action(detail=False, methods=['patch'])
    def mark_all_as_read(self, request):
        notifications = Notification.objects.filter(user=request.user, is_read=False)
        count = notifications.update(is_read=True)
        return Response(
            {"message": f"{count} notification(s) marquée(s) comme lue(s)."},
            status=status.HTTP_200_OK
        )
