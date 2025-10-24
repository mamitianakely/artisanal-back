# api/administrateur/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from api.payement.models import Payement
from api.produit.models import Produit

@api_view(['GET'])
def total_transactions(request):
    total = Payement.objects.aggregate(total_montant=Sum('montant'))['total_montant'] or 0
    return Response({"total_transactions": total})

@api_view(['GET'])
def total_produits(request):
    total = Produit.objects.count()
    return Response({"total_produits": total})

@api_view(['GET'])
def transactions_recentes(request):

    # Types correspondant aux radios du frontend
    types = ['Telma', 'Airtel', 'Orange']
    result = []

    for t in types:
        dernier = (
            Payement.objects.filter(typePayement__iexact=t)
            .order_by('-datePayement')  # date décroissante
            .values('typePayement', 'montant', 'datePayement')[:1]
        )
        if dernier:
            dernier_payement = dernier[0]
            # Avatar coloré pour le frontend
            avatar = '🟢' if t.lower() == 'telma' else '🔴' if t.lower() == 'airtel' else '🟠'
            result.append({
                'title': f"Paiement {dernier_payement['typePayement']}",
                'amount': f"+{dernier_payement['montant']} Ar",
                'avatar': avatar
            })

    return Response(result)

@api_view(['GET'])
def repartition_payements(request):
    types = ['Telma', 'Airtel', 'Orange']
    result = []

    for t in types:
        total = Payement.objects.filter(typePayement__iexact=t).aggregate(total=Sum('montant'))['total'] or 0
        result.append({
            'type': t,
            'value': total
        })

    return Response(result)

# --- Liste complète des paiements avec nom client et nom produit ---
@api_view(['GET'])
def liste_paiements(request):
    paiements = Payement.objects.all().order_by('-datePayement')  # trier par date décroissante
    result = []

    for p in paiements:
        result.append({
            'id_payement': p.id_payement,
            'montant': p.montant,
            'typePayement': p.typePayement,
            'datePayement': p.datePayement,
            'id_commande': p.id_commande_id if p.id_commande_id else None,
            'id_user': p.id_user_id if p.id_user_id else None,
        })

    return Response(result)