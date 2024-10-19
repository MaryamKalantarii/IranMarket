from django.urls import path,include

app_name = "clothing"

urlpatterns = [
    path("",include("product.clothing.urls.clothingurls")),
 
 
]