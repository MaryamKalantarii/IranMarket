from django.urls import path, include
from ..views.profiles import*


urlpatterns = [
    path("home/",CustomerDashboardHomeView.as_view(), name="home"),
    path("security-edit/",CustomerSecurityEditView.as_view(), name="security-edit"),
    path("profile/edit/",CustomerProfileEditView.as_view(),name="profile-edit"),
    path("profile/image/edit/",CustomerProfileImageEditView.as_view(),name="profile-image-edit"),
]
