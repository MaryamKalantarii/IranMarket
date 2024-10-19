from django.urls import path,include

app_name = "dijitalgoods"

urlpatterns = [
    path("",include("product.dijitalgoods.urls.dijitalgoods_urls")),
 
 
]