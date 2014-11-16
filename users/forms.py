from django import forms
from django.forms import Form


class LoginForm(Form):
    login = forms.CharField(initial='login')
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
            'password': forms.PasswordInput(),
        }