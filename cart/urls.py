from django.urls import path
from .views import *


app_name = 'cart'


urlpatterns =[
    path("session/add-product/",SessionAddProduct.as_view(), name = "session-add-product"),
    path("session/cart/summary",SessionCartSummary.as_view(), name = "session-cart-summary"),

]    