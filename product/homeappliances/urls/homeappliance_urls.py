from django.urls import path,re_path
from ..views.homeappliance_views import *

urlpatterns =[
    re_path(r"categoy-detaile/(?P<slug>[-\w]+)/",homeappliances_detaile.as_view(),name="categoy-detaile"),
    path("category-grid/",HomeapplianceGrid.as_view(),name="category-grid"),
    path("category-clothing/",HomeapplianceView.as_view(),name="category-homeappliances"),
]
