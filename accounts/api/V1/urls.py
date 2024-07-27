from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "api-v1-accounts"

urlpatterns = [

    path("registration/", RegistrationView.as_view(), name="registration"),
    path("is-verified/<str:token>", IsVerifiedView.as_view(), name="is-verification"),
    path("resend-email/", ResendEmailView.as_view(), name="resend-email"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("reset-password-email/",ResetPasswordEmailView.as_view(),name="reset-password-email"),
    path("reset-password/<str:token>", ResetPasswordView.as_view(), name="reset-password"),
    
    # jwt token
    path("token/login/", CustomeTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]