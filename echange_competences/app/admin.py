from django.contrib import admin

from .models import Skill, Profil, RequestHelp, OfferHelp

# Register your models here.
admin.site.register(Skill)
admin.site.register(Profil)
admin.site.register(RequestHelp)
admin.site.register(OfferHelp)
