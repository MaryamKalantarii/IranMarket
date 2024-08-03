from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/',signup, name='signup'),
    path('otp-verify/', OtpVerifyView.as_view(), name='otp-verify'),
    path('login/', LoginView.as_view(), name='login'),
    
    path('api/V1/',include("accounts.api.V1.urls")),

]


