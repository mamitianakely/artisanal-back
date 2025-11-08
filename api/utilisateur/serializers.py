# app/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Utilisateur, Client, Vendeur
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id_user', 'nom', 'email', 'role', 'is_active', 'is_staff']
        read_only_fields = ['id_user', 'is_active', 'is_staff']

class UtilisateurCreateSerializer(serializers.ModelSerializer):
    # on accepte motDePasse ou password (compatibilité FR)
    motDePasse = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Utilisateur
        fields = ['id_user', 'nom', 'email', 'role', 'motDePasse', 'password']
        read_only_fields = ['id_user']

    def create(self, validated_data):
        motDePasse = validated_data.pop('motDePasse', None) or validated_data.pop('password', None)
        return Utilisateur.objects.create_user(email=validated_data['email'],
                                               motDePasse=motDePasse,
                                               nom=validated_data.get('nom'),
                                               role=validated_data.get('role', 'client'))

class ClientSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(read_only=True)
    class Meta:
        model = Client
        fields = ['utilisateur', 'adresse', 'telephone']

class VendeurSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(source='utilisateur_ptr.nom', read_only=True)
    email = serializers.EmailField(source='utilisateur_ptr.email', read_only=True)
    role = serializers.CharField(source='utilisateur_ptr.role', read_only=True)

    class Meta:
        model = Vendeur
        fields = ['id_user', 'nom', 'email', 'role', 'entreprise', 'contact']


# Token serializer (ajoute role et id_user au payload de réponse)
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # ajouter des claims si besoin
        token['role'] = user.role
        token['id_user'] = user.id_user
        return token

    def validate(self, attrs):
        # supporte 'motDePasse' ou 'password' comme clé côté client
        credentials = {
            'username': attrs.get(self.username_field),
            'password': attrs.get('password') or attrs.get('motDePasse')
        }

        if credentials['username'] and credentials['password']:
            user = authenticate(request=self.context.get('request'),
                                username=credentials['username'],
                                password=credentials['password'])
            if not user:
                raise serializers.ValidationError("Email ou mot de passe incorrect")
        else:
            raise serializers.ValidationError("Email et mot de passe requis")

        data = super().validate({'email': credentials['username'], 'password': credentials['password']})
        # on ajoute role et id_user à la réponse
        data['role'] = user.role
        data['id_user'] = user.id_user
        data['nom'] = user.nom
        return data
