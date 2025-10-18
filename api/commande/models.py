from django.db import models
from api.utilisateur.models import Client

def generate_commande_id():
    last_commande = Commande.objects.order_by('id_commande').last()
    if not last_commande:
        return "COM001"
    commande_num = int(last_commande.id_commande.replace("COM", "")) + 1
    return f"COM{commande_num:03d}"

class Commande(models.Model):
    id_commande = models.CharField(primary_key=True, max_length=10, editable=False)
    dateCommande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50)
    total = models.FloatField()
    id_user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='commandes')

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def save(self, *args, **kwargs):
        if not self.id_commande:
            self.id_commande = generate_commande_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Commande {self.id_commande} - {self.dateCommande.strftime('%Y-%m-%d %H:%M')}"