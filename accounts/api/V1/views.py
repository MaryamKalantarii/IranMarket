from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .multi_threading import SendEmailWithThreading
from accounts.models import CustomeUser,Profail
from rest_framework.permissions import IsAuthenticated
from .serializer import (
            RegisterationSerializer,
            ResendEmailSerializer,
            CustomTokenObtainPairSerializer,
            PasswordChangeSerializer,
            ProfailSerializer,
            ResetPasswordEmailSerializer,
            ResetPasswordSerializer,
            )  


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


class IsVerifiedView(GenericAPIView):
    
    def get(self , request, *args, **kwargs):

        try:
            user_data = AccessToken(kwargs.get("token"))
            user_id = user_data["user_id"]
            user = get_object_or_404(CustomeUser,id = user_id)
            user.is_verified = True
            user.save()
            return Response({"detail":"email verified successfully"})
        except Exception:
            return Response(
                {
                    "detail": "your token may be expired or changed structure",
                    "resend email": "http://127.0.0.1:8000/accounts/api/V1/resend-email",
                }
            )


class ResendEmailView(GenericAPIView):

    serializer_class = ResendEmailSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        if user.is_verified:
            return Response({"detail":"email already verified"})
        
        token = self.get_token_for_user(user)
        message = EmailMessage("email/email.html",{"token":token},"maryam@admin.com",to=[user.email],)
        email = SendEmailWithThreading(message)
        email.start()
        return Response({"detail":"email Resend for your verification"})

    def get_token_for_user(self,user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomeTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class ChangePasswordView(GenericAPIView):
     
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChangeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.check_old_password(request,serializer.validated_data)
        serializer.set_new_password(request,serializer.validated_data)

        return Response({"detail":"password changed successfully"},
        status=status.HTTP_200_OK,
        
        )

class ProfileView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfailSerializer
    queryset = Profail.objects.all()

    def get(self, request, *args, **kwargs):
        user = request.user
        profail = get_object_or_404(Profail, user=user)
        serializer = self.serializer_class(profail)
        return Response(data = serializer.data , status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        user = request.user
        profail = get_object_or_404(Profail,user=user)
        serializer = self.serializer_class(profail, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data = serializer.data , status=status.HTTP_200_OK)
    


class ResetPasswordEmailView(GenericAPIView):
    serializer_class = ResetPasswordEmailSerializer

    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = self.get_tokens_for_user(user)
        message = EmailMessage("email/reset_password.html",{"token": token},"maryam@admin.com",to = [serializer.validated_data["email"]],)
        email = SendEmailWithThreading(message)
        email.start()
        return Response({"detail":"email send for you"})
    
    def get_tokens_for_user(self, user):

        refresh=RefreshToken.for_user(user)
        return str(refresh.access_token)
    


class ResetPasswordView(GenericAPIView):

    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):

        try:
            user_data = AccessToken(kwargs.get("token"))
            user_id = user_data["user_id"]
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.set_new_password(request,serializer.validated_data)
            token = serializer.create_new_token(request,serializer.validated_data)

            return Response(
                data={"detail":"password changed successfully","token":token.key},
                status = status.HTTP_200_OK
            )
        except Exception:
            (
            {
                "detail": "your token may be expired or changed structure...",
                "resend email": "http://127.0.0.1:8000/accounts/api/V1/resend-email",
            }
        ) 