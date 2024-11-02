from django.urls import path,include

app_name = "appliances"

urlpatterns = [
    path("",include("product.appliances.urls.appliances_url")),
 
 
]