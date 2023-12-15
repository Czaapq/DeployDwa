from django.contrib import admin
from .models import Bibik

# admin.site.register(Bibik)


@admin.register(Bibik)
class BibikAdmin(admin.ModelAdmin):
    list_display = ["imie", "pseudonim", "ocena1na10"]
