from django.urls import path, include
from .views import*

app_name = 'customer'
urlpatterns = [

    path("home/",CustomerDashboardHomeView.as_view(), name="home"),
    path("security-edit/",CustomerSecurityEditView.as_view(), name="security-edit"),
    path("profile/edit/",CustomerProfileEditView.as_view(),name="profile-edit"),
]