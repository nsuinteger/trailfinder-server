from django import forms
from item.models import Item


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item



class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item