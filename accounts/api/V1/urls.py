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
    path("resend/", ResendEmailView.as_view(), name="resend"),
    
    # jwt token
    path("token/login/", CustomeTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]