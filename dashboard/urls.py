from django.urls import path,include
from .views import *
app_name = 'dashboard'

urlpatterns = [
    path("dashboard",DashboardHomeView.as_view(),name="dashboard"),


]