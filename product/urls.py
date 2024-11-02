from django.urls import path,include,re_path
from .views import *
from . import views

app_name = 'product'
urlpatterns =[
    
    # include clothing urls
    path("clothing/",include('product.clothing.urls')),

    # include dijitalgoods urls
    path("dijitalgoods/",include('product.dijitalgoods.urls')),

    path("homeappliances/",include('product.homeappliances.urls')),

    path("beauty/",include('product.beauty.urls')),


    # path("child/",include('product.child.urls')),

    path("supermarket/",include('product.supermarket.urls')),

    path("appliances/",include('product.appliances.urls')),


    path("search/",search_products,name="search_products"),


   
    


    # path('api/V1/',include("product.api.V1.urls")),
]