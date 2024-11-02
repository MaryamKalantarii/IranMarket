from django.urls import path,include

app_name = "supermarket"

urlpatterns = [
    path("",include("product.supermarket.urls.supermarket_url")),
 
 
]