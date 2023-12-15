from django.forms import ModelForm
from .models import Bibik

class BibikForm(ModelForm):
    class Meta:
        model = Bibik
        fields = ['imie','pseudonim','ocena1na10','opis']