from django.db import models
from api.category.models import Category
from api.utilisateur.models import Vendeur

def generate_produit_id():
    last_produit = Produit.objects.order_by('id_produit').last()
    if not last_produit:
        return "PRD001"
    produit_num = int(last_produit.id_produit.replace("PRD", "")) + 1
    return f"PRD{produit_num:03d}"

class Produit(models.Model):
    id_produit = models.CharField(primary_key=True, max_length=10, editable=False)
    nomProduit = models.CharField(max_length=255)
    descriptionProduit = models.TextField(blank=True)
    prixUnitaire = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='produits/', blank=True, null=True)
    datePublication = models.DateTimeField(auto_now_add=True)
    id_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='produits')
    id_user = models.ForeignKey(Vendeur, on_delete=models.CASCADE, related_name='produits')

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def save(self, *args, **kwargs):
        if not self.id_produit:
            self.id_produit = generate_produit_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nomProduit