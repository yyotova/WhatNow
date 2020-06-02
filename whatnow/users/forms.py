from django import forms
# from .models import Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=8)
    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput, min_length=8)
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', "phone", "password1", "password2"]

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = Users.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("email is taken")
    #     return email

    # def clean_password2(self):
    #     password = self.cleaned_data.get("password")
    #     password2 = self.cleaned_data.get("password2")
    #     if password and password2 and password != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password
