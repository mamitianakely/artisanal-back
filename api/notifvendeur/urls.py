# api/notifvendeur/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotifVendeurViewSet

router = DefaultRouter()
router.register(r'notifvendeur', NotifVendeurViewSet, basename='notifvendeur')

urlpatterns = [
    path('', include(router.urls)),
]
