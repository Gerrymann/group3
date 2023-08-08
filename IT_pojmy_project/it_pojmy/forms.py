from django import forms
from it_pojmy.models import Clanek


class ClanekForm(forms.ModelForm):
    class Meta:
        model = Clanek
        fields = ['slug', 'nazev', 'popis', 'kategorie']