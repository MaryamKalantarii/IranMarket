from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/',SignUpView.as_view(), name='signup'),
    path('otp-verify/', OtpVerifyView.as_view(), name='otp-verify'),
    path('login/', LoginView.as_view(), name='login'),
]


