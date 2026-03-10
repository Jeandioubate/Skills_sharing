
from django.db import models
from django.contrib.auth.models import User

"""
Implémentation des modèles de données en fonction du diagramme de classes

"""
# Création de la classe compétence

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# La classe utilisateur

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user.username

# La classe activité ou demande d'aide

class RequestHelp(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    required_skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    description = models.TextField()
    slot = models.DateField()
    help_found = models.BooleanField(default=False)

    def __str__(self):
        return self.description

# La classe Proposition d'aide (l'utilisateur se rend disponible pour aider)

class OfferHelp(models.Model):
    request = models.OneToOneField(RequestHelp, on_delete=models.CASCADE)
    helper = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Aide pour {self.request}"




