from django import forms
from django.forms import ModelForm
from .models import RegProfile


class RegForm(ModelForm):
    class Meta:
        model = RegProfile
        fields = '__all__'
        widgets = {'loft_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Loft Name"}),
                   'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
                   'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
                   'zip_code': forms.TextInput(attrs={"class": "form-control", "placeholder": "ZIP Code"}),
                   'mobile_number': forms.TextInput(attrs={"class": "form-control", "placeholder": "Mobile Number"}),
                   'email': forms.TextInput(attrs={"class": "form-control", "placeholder": "Email Address"})
                   }

