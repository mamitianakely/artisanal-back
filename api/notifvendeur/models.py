# models/notifvendeur.py
from django.db import models
from api.utilisateur.models import Utilisateur
from api.produit.models import Produit  # Si tu as un modèle Produit
import uuid

def generate_id_notif():
    return uuid.uuid4().hex[:10]

class NotifVendeur(models.Model):
    id_notif = models.CharField(
        primary_key=True,
        max_length=10,
        default=generate_id_notif,
        editable=False
    )
    user = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name="notifvendeurs"
    )
    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    message = models.TextField()
    type = models.CharField(
        max_length=20,
        choices=[('validation', 'Validation'), ('refus', 'Refus')]
    )
    is_read = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.nom} - {self.type} - {self.date_creation.strftime('%Y-%m-%d %H:%M')}"
