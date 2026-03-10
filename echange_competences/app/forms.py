
from django import forms
from .models import RequestHelp, Profil

"""
Implémentation des formulaires dans forms.py
"""

# Formulaire demande d'aide ou activité

class RequestHelpForm(forms.ModelForm):

    class Meta:
        model = RequestHelp

        fields = [
            "skill",
            "description",
            "slot"
        ]

# Formulaire pour renseigner les compétences

class SkillForm(forms.ModelForm):

    class Meta:
        model = Profil

        fields = ["skills"]

        widgets = {
            "skills": forms.CheckboxSelectMultiple()
        }