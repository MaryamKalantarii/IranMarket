from django.urls import path,re_path
from .views import *

app_name = "payment"

urlpatterns = [
    path("verify",PaymentVerifyView.as_view(),name="verify"),


]