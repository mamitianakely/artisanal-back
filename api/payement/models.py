from django.db import models
from api.commande.models import Commande
from api.utilisateur.models import Client

def generate_payement_id():
    last_payement = Payement.objects.order_by('id_payement').last()
    if not last_payement:
        return "PAY001"
    payement_num = int(last_payement.id_payement.replace("PAY", "")) + 1
    return f"PAY{payement_num:03d}"

class Payement(models.Model):
    id_payement = models.CharField(primary_key=True, max_length=10, editable=False)
    montant = models.FloatField()
    typePayement = models.CharField(max_length=30)
    datePayement = models.DateTimeField(auto_now_add=True)
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='payement')
    id_user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='payement')

    class Meta:
        verbose_name = "Paiement"
        verbose_name_plural = "Paiements"

    def __str__(self):
        return f"Paiement {self.id_paiement} - {self.montant} Ar ({self.typePayement})"