from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/',signup, name='signup'),
    path('otp-verify/', OtpVerifyView.as_view(), name='otp-verify'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('login-password/', Login_password.as_view(), name='login-password'),

    path('profile/', Profile_View.as_view(),name='profile'),



    path('api/V1/',include("accounts.api.V1.urls")),

]


