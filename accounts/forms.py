from django import forms
from .models import CustomeUser, Profile


class CustomUserCreation(UserCreationForm):

    class Meta:
        model = CustomeUser
        fields = ["email"]