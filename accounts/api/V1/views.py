from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializer import RegisterationSerializer        
from .multi_threading import SendEmailWithThreading
from accounts.models import CustomeUser,Profail

class  RegistrationView(GenericAPIView):
    serializer_class = RegisterationSerializer

    def post(self, request,*args,**kwargs):
        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_object_or_404(CustomeUser , email = serializer.validated_data["email"])
            token = self.get_token_for_user(user)
            message = EmailMessage("email/email.html",{"token":token},"maryam@admin.com",to=[serializer.validated_data["email"]],)
            email = SendEmailWithThreading(message)
            email.start()
            return Response({"detail":"email send for your verification"})

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get_token_for_user(self,user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


        