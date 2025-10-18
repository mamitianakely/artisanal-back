from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LigneCommandeViewSet

router = DefaultRouter()
router.register(r'', LigneCommandeViewSet, basename='lignecommande')

urlpatterns = [
    path('', include(router.urls)),
]
