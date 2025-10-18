from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid

def generate_id_user():
    return uuid.uuid4().hex[:10]

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, motDePasse=None, role='client', nom=None, **extra_fields):
        if not email:
            raise ValueError("L'utilisateur doit avoir un email")
        email = self.normalize_email(email)
        user = self.model(email=email, nom=nom, role=role, **extra_fields)
        user.set_password(motDePasse)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, motDePasse, nom="Admin", **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, motDePasse, nom=nom, role='admin', **extra_fields)

class Utilisateur(AbstractBaseUser, PermissionsMixin):
    id_user = models.CharField(primary_key=True, max_length=10, editable=False, default=generate_id_user)
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=[
        ('client', 'Client'),
        ('vendeur', 'Vendeur'),
        ('admin', 'Administrateur')
    ])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom']

    def __str__(self):
        return f"{self.nom} ({self.role})"

    @property
    def id(self):
        return self.id_user

# --- Héritage réel ---
class Client(Utilisateur):
    adresse = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=20, blank=True)

class Vendeur(Utilisateur):
    entreprise = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=20, blank=True)
