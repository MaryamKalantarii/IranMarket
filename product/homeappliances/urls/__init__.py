from django.urls import path,include

app_name = "homeappliances"

urlpatterns = [
    path("",include("product.homeappliances.urls.homeappliance_urls")),
 
 
]