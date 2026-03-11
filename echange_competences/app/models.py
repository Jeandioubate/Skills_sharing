
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Classe compétence

class Skill(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Profil utilisateur

class Profil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user.username


# Demande d'aide

class RequestHelp(models.Model):

    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    required_skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    description = models.TextField()

    slot = models.DateField()

    help_found = models.BooleanField(default=False)

    def __str__(self):

        return f"{self.description} ({self.slot})"


# Proposition d'aide

class OfferHelp(models.Model):

    request = models.OneToOneField(RequestHelp, on_delete=models.CASCADE)

    helper = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return f"Aide pour {self.request}"


# Création automatique du profil

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:

        Profil.objects.create(user=instance)








