from rest_framework import serializers
from .models import Utilisateur, Client, Vendeur

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['utilisateur', 'adresse', 'telephone']

class VendeurSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer(read_only=True)

    class Meta:
        model = Vendeur
        fields = ['utilisateur', 'entreprise', 'contact']