from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Payement
from api.commande.models import Commande

# ----------------------------
# 1️⃣ Simulation de paiement
# ----------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def simuler_payement(request):
    user = request.user  # utilisateur connecté

    # Seul un client peut effectuer un paiement
    if not hasattr(user, 'role') or user.role != 'client':
        return Response({'error': 'Seul un client peut effectuer un paiement.'}, status=403)

    montant = request.data.get('montant')
    typePayement = request.data.get('typePayement')
    id_commande = request.data.get('id_commande')

    if not all([montant, typePayement, id_commande]):
        return Response({'error': 'Données incomplètes'}, status=400)

    # Vérifier que la commande existe et appartient à l'utilisateur
    try:
        commande = Commande.objects.get(id_commande=id_commande, id_user=user)
    except Commande.DoesNotExist:
        return Response({'error': "Commande introuvable ou non autorisée."}, status=400)

    # Vérifier que la commande est validée
    if commande.statut.lower() != 'validée':
        return Response({'error': "La commande n'est pas encore validée par le vendeur."}, status=400)

    # Créer le paiement
    payement = Payement.objects.create(
        montant=montant,
        typePayement=typePayement,
        id_commande=commande,
        id_user=user
    )

    return Response({
        'message': 'Paiement simulé avec succès',
        'id_payement': payement.id_payement,
        'montant': payement.montant,
        'typePayement': payement.typePayement,
        'datePayement': payement.datePayement,
    })


# ----------------------------
# 2️⃣ Récupérer une commande validée
# ----------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_commande_validee(request, id_commande):
    user = request.user

    # Vérifier que la commande existe et appartient à l'utilisateur
    try:
        commande = Commande.objects.get(id_commande=id_commande, id_user=user)
    except Commande.DoesNotExist:
        return Response({'error': 'Commande introuvable ou non autorisée.'}, status=404)

    # Vérifier que la commande est validée
    if commande.statut.lower() != 'validée':
        return Response({'error': 'Cette commande n’est pas encore validée.'}, status=400)

    return Response({
        'id_commande': commande.id_commande,
        'montant': commande.total,  # <-- montant réel de la commande
        'statut': commande.statut,
        'dateCommande': commande.dateCommande,
    })
