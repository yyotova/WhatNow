from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', "phone", "password1", "password2"]
