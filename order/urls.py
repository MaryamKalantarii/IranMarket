from django.urls import path, include
from .views import*

app_name = "order"

urlpatterns = [
    path("checkout/",OrderCheckOutView.as_view(), name="checkout"),
    
]
