from django.db import models

class Utilisateur(models.Model):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('vendeur', 'Vendeur'),
        ('admin', 'Administrateur')
    ]

    id_user = models.CharField(primary_key=True, max_length=10, editable=False)
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    motDePasse = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def save(self, *args, **kwargs):
        # Générer l'id_user si ce n'est pas défini
        if not self.id_user:
            last_user = Utilisateur.objects.order_by('id_user').last()
            if not last_user:
                self.id_user = "USR001"
            else:
                user_num = int(last_user.id_user.replace("USR", "")) + 1
                self.id_user = f"USR{user_num:03d}"

        is_new = self._state.adding
        super().save(*args, **kwargs)

        # Création automatique de l'entrée associée
        if is_new:
            if self.role == "client":
                Client.objects.create(utilisateur=self)
            elif self.role == "vendeur":
                Vendeur.objects.create(utilisateur=self)

    def __str__(self):
        return f"{self.nom} ({self.role})"


class Client(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key=True)
    adresse = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.utilisateur.nom


class Vendeur(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key=True)
    entreprise = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.utilisateur.nom
