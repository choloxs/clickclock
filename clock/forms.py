from django import forms
from django.forms import ModelForm
from .models import Roll


class RollForm(ModelForm):
    class Meta:
        model = Roll
        fields = ('race', 'code')
        labels = {'race': 'Select Race', 'code': ''}
        widgets = {'code': forms.TextInput(attrs={"class": "form-control", "placeholder": "Registration ID/Code"})}

