from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser


class CustomUserCreation(UserCreationForm):

    class Meta:
        model = CustomeUser
        fields = ["username","password1","password2"]


class OtpForm(forms.Form):
    otp_code =forms.CharField(max_length=4)


class LoginForm(forms.Form):
    email = forms.EmailField()


class AuthenticationForm(forms.Form):
    
    email = forms.EmailField()
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )