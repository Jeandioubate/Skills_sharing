
from django.urls import path
from . import views

"""
Mise en place des URLs pour chaque vue
"""

app_name = "app"

urlpatterns = [
    path("", views.home, name="home"),
    path("skills/", views.skills_list, name="skills_list"),
    path("my-skills/", views.my_skills, name="my_skills"),
    path("demande/", views.create_request, name="create_request"),
    path("demandes/", views.request_available, name="request_available"),
    path("offer_help/<int:demande_id>/", views.offer_help, name="offer_help"),
]