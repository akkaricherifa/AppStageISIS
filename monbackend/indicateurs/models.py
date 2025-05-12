from django.db import models
from django.contrib.auth.models import User

class Indicateur(models.Model):
    titre = models.CharField(max_length=200)
    Axe = models.TextField(blank=True, null=True)
    Fiche = models.FloatField()
    Action = models.CharField(max_length=50)
    unite_mesure = models.DateField()
    periodicite_mesure = models.CharField(max_length=200)
    dernier_resultat_connu = models.TextField(blank=True, null=True)
    nature_donnees = models.FloatField()
    source_donnees = models.CharField(max_length=50)
    service_responsable_donnees = models.DateField()
    validation = models.BooleanField(default=False)
    mode_calcul = models.CharField(max_length=200)
    modalite_donnees = models.TextField(blank=True, null=True)
    limite = models.FloatField()
    modalite_interprétation = models.CharField(max_length=50)
    date_indicateur = models.DateField()
    amelioration_indicateur = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titre} - {self.valeur} {self.unite}"




class Profil(models.Model):
    USER_ROLES = [
        ('admin', 'Administrateur'),
        ('responsable', 'Responsable'),
        ('observateur', 'Observateur'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
