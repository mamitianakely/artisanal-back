# project/urls.py ou app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'utilisateurs', views.UtilisateurViewSet, basename='utilisateur')

urlpatterns = [
    path('', include(router.urls)),
    path('me/', views.current_user, name='current_user'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('utilisateurs/role/<str:role>/', views.utilisateurs_par_role, name='utilisateurs_par_role'),
    path('me_vendeur/', views.me_vendeur, name='me_vendeur'),
]

