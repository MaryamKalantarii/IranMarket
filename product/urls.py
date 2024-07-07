from django.urls import path,include
from .views import *


app_name = 'product'
urlpatterns =[
    # path("",ProductView.as_view(),name="products"),
    path("category-clothing/",ClothingView.as_view(),name="category-clothing"),
    path("category-dijitalgoods/",DijitalgoodsView.as_view(),name="category-dijitalgoods"),
    path("category-homeappliances/",HomeappliancesView.as_view(),name="category-homeappliances"),
    path("category-clothing/",ClothingView.as_view(),name="category-clothing"),
    path("category-clothing/",ClothingView.as_view(),name="category-clothing"),
    path("category-clothing/",ClothingView.as_view(),name="category-clothing"),
    path("category-clothing/",ClothingView.as_view(),name="category-clothing"),



    
    path("singleProduct/", Product_single_View.as_view(),name="singleProduct"),
    path('api/V1/',include("product.api.V1.urls")),
]