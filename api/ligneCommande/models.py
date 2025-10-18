from django.db import models
from api.commande.models import Commande
from api.produit.models import Produit

def generate_ligneCommande_id():
    last_ligne = LigneCommande.objects.order_by('id_ligne').last()
    if not last_ligne:
        return "LIN001"
    ligne_num = int(last_ligne.id_ligne.replace("LIN", "")) + 1
    return f"COM{ligne_num:03d}"

class LigneCommande(models.Model):
    id_ligne = models.CharField(primary_key=True, max_length=10, editable=False)
    quantiteCommande = models.FloatField()
    sousTotal = models.FloatField()
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='ligneCommandes')
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='ligneCommandes')

    class Meta:
        verbose_name = "LigneCommande"
        verbose_name_plural = "LigneCommandes"

    def save(self, *args, **kwargs):
        if not self.id_ligne:
            self.id_ligne = generate_ligneCommande_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"LigneCommande {self.quantiteCommande}"