from django.urls import path, include
from .views import*

app_name = "order"

urlpatterns = [
    path("checkout/",OrderCheckOutView.as_view(), name="checkout"),
    path("completed/",OrderCompletedView.as_view(),name="completed"),
    path("validate-coupon/",ValidateCouponView.as_view(),name="validate-coupon"),
    
]
