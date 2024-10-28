from django.urls import path, include
from .views import*

app_name = 'customer'
urlpatterns = [

    path("home/",CustomerDashboardHomeView.as_view(), name="home"),
]