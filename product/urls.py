from django.urls import path,include
from .views import *


app_name = 'product'
urlpatterns =[
    # path("",ProductView.as_view(),name="products"),
    path("category-clothing/",ClothingView.as_view(),name="category-clothing"),
    path("category-grid/",ClothingGrid.as_view(),name="category-grid"),
    path("categoy-detaile/",Clothing_detaile.as_view(),name="categoy-detaile"),


    path("category-dijitalgoods/",DijitalgoodsView.as_view(),name="category-dijitalgoods"),
    path("category-homeappliances/",HomeappliancesView.as_view(),name="category-homeappliances"),
    path("category-beauty/", BeautyView.as_view(),name="category-beauty"),
    path("category-appliances/",AppliancesView.as_view(),name="category-appliances"),
    path("category-supermarket/",SupermarketView.as_view(),name="category-supermarket"),
    path("category-child/",Child_and_babyView.as_view(),name="category-child"),

    


    
    path("singleProduct/", Product_single_View.as_view(),name="singleProduct"),
    path('api/V1/',include("product.api.V1.urls")),
]