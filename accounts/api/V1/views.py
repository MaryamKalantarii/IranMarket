from rest_framework.generics import GenericAPIView
from rest_framework.response import responses
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializer import RegisterationSerializer        
from .multi_threading import SendEmailWithThreading
from accounts.models import CustomeUser,Profail

class  RegistrationView(GenericAPIView):
    pass
