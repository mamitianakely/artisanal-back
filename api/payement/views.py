from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Payement
import random

@api_view(['POST'])
def simuler_payement(request):
    montant = request.data.get('montant')
    typePayement = request.data.get('typePayement')
    id_commande = request.data.get('id_commande')
    id_user = request.data.get('id_user')

    if not all([montant, typePayement, id_commande, id_user]):
        return Response({'error' : 'Données incomplètes'}, status=400)

    payement = Payement.objects.create(
        montant=montant,
        typePayement=typePayement,
        id_commande=id_commande,
        id_user=id_user,
    )

    return Response({
        'message' : 'Paiement simulé avec succès',
        'id_payement' : payement.id_payement,
        'montant' : payement.montant,
        'typePayement' : payement.typePayement,
        'datePayement' : payement.datePayement,
    })