from django.db import models
from api.produit.models import Produit


def generate_promotion_id():
    last_promotion = Promotion.objects.order_by('id_prom').last()
    if not last_promotion:
        return "PROM001"
    prom_num = int(last_promotion.id_prom("PROM", "")) + 1
    return f"PROM{prom_num:03d}"

class Promotion(models.Model):
    id_prom = models.CharField(primary_key=True, max_length=10, editable=False)
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='promotions')
    prixAvant = models.DecimalField(max_digits=10, decimal_places=2)
    prixApres = models.DecimalField(max_digits=10, decimal_places=2)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Promotion {self.produit.nom} ({self.prixAvant} → {self.prixApres})"