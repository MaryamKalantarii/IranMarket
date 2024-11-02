from django.urls import path,include,re_path
from ..views.appliances_view import *

urlpatterns =[
    re_path(r"categoy-detaile/(?P<slug>[-\w]+)/",Appliances_detaile.as_view(),name="categoy-detaile"),
    path("category-grid/",AppliancesGrid.as_view(),name="category-grid"),
    path("category-appliances/",AppliancesView.as_view(),name="category-appliances"),
]
