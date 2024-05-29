from django.urls import path,include
from .views import *


app_name = 'product'
urlpatterns =[
    path("",ProductView.as_view(),name="products"),
    path("index-Product/",Product_index_View.as_view(),name="index-Product"),
    path("singleProduct/", Product_single_View.as_view(),name="singleProduct"),
    path('api/V1/',include("product.api.V1.urls")),
]