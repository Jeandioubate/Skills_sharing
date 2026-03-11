
from django import forms
from .models import RequestHelp, Profil

"""
Implémentation des formulaires
"""

# Formulaire demande d'aide

class RequestHelpForm(forms.ModelForm):

    class Meta:

        model = RequestHelp

        fields = [
            "required_skill",
            "description",
            "slot"
        ]


# Formulaire gestion des compétences

class CompetenceForm(forms.ModelForm):

    class Meta:

        model = Profil

        fields = ["skills"]

        widgets = {
            "skills": forms.CheckboxSelectMultiple()
        }