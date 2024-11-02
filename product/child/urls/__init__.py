from django.urls import path,include

app_name = "child"

urlpatterns = [
    path("",include("product.child.urls.child_url")),
 
 
]