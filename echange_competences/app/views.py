
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RequestHelpForm, CompetenceForm
from .models import RequestHelp, Skill, OfferHelp


"""
Implémentation des différentes vues
"""

# Page d'accueil

def home(request):

    slots = RequestHelp.objects.filter(help_found=True).order_by("slot")

    skills = Skill.objects.all()

    return render(request, "app/home.html", {"slots": slots, "skills": skills})


# Liste des compétences

def skills_list(request):

    skills = Skill.objects.all()

    return render(request, "app/skills.html", {"skills": skills})


# Compétences de l'utilisateur

@login_required
def my_skills(request):

    profil = request.user.profil

    if request.method == "POST":

        form = CompetenceForm(request.POST, instance=profil)

        if form.is_valid():
            form.save()

    else:

        form = CompetenceForm(instance=profil)

    return render(request, "app/my_skills.html", {"form": form})


# Création d'une demande d'aide

@login_required
def create_request(request):

    if request.method == "POST":

        form = RequestHelpForm(request.POST)

        if form.is_valid():

            demande = form.save(commit=False)

            demande.applicant = request.user

            demande.save()

            return redirect("app:home")

    else:

        form = RequestHelpForm()

    return render(request, "app/create_request.html", {"form": form})


# Voir les demandes correspondant aux compétences

@login_required
def request_available(request):

    profil = request.user.profil

    demandes = RequestHelp.objects.filter(
        required_skill__in=profil.skills.all(),
        help_found=False
    )

    return render(request, "app/request_available.html", {"demandes": demandes})


# Se proposer pour aider

@login_required
def offer_help(request, demande_id):

    demande = RequestHelp.objects.get(id=demande_id)

    OfferHelp.objects.create(
        request=demande,
        helper=request.user
    )

    demande.help_found = True
    demande.save()

    return redirect("app:request_available")

# Afficher les demandes d'aide du même utilisateur

@login_required
def my_requests(request):

    demandes = RequestHelp.objects.filter(applicant=request.user).order_by("-slot")

    return render(request, "app/my_requests.html", {"demandes": demandes})