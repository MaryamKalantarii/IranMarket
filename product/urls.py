from django.urls import path,include,re_path
from .views import *
from . import views

app_name = 'product'
urlpatterns =[
    
    # include clothing urls
    path("clothing/",include('product.clothing.urls')),

    # include dijitalgoods urls
    path("dijitalgoods/",include('product.dijitalgoods.urls')),

    path("category-homeappliances/",HomeappliancesView.as_view(),name="category-homeappliances"),
    path("category-beauty/", BeautyView.as_view(),name="category-beauty"),
    path("category-appliances/",AppliancesView.as_view(),name="category-appliances"),
    path("category-supermarket/",SupermarketView.as_view(),name="category-supermarket"),
    path("category-child/",Child_and_babyView.as_view(),name="category-child"),

    


    
    path("singleProduct/", Product_single_View.as_view(),name="singleProduct"),
    # path('api/V1/',include("product.api.V1.urls")),
]