
from django.contrib import admin
from .models import Skill, Profil, RequestHelp, OfferHelp


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ("user",)
    filter_horizontal = ("skills",)


@admin.register(RequestHelp)
class RequestHelpAdmin(admin.ModelAdmin):
    list_display = ("description", "required_skill", "slot", "help_found")
    list_filter = ("required_skill", "help_found")


@admin.register(OfferHelp)
class OfferHelpAdmin(admin.ModelAdmin):
    list_display = ("request", "helper")