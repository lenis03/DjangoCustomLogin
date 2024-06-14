from django import forms

from .models import CustomUser


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
