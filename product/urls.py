from django.urls import path
from .views import *


app_name = 'product'
urlpatterns =[
    path("product/",ProductView.as_view(),name="Product"),
]