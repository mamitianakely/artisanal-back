from rest_framework import viewsets, status
from .models import Utilisateur, Client, Vendeur
from .serializers import UtilisateurSerializer, ClientSerializer, VendeurSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class VendeurViewSet(viewsets.ModelViewSet):
    queryset = Vendeur.objects.all()
    serializer_class = VendeurSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        motDePasse = request.data.get("motDePasse")

        try:
            utilisateur = Utilisateur.objects.get(email=email)
            if utilisateur.motDePasse == motDePasse:
                return Response({
                    "message": "Connexion réussie",
                    "user": {
                        "id_user": utilisateur.id_user,
                        "nom": utilisateur.nom,
                        "email": utilisateur.email,
                        "role": utilisateur.role
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Mot de passe incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
        except Utilisateur.DoesNotExist:
            return Response({"error": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)
