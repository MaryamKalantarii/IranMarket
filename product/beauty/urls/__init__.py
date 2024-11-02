from django.urls import path,include

app_name = "beauty"

urlpatterns = [
    path("",include("product.beauty.urls.beauty_url")),
 
 
]