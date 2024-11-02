from django.urls import path,include,re_path
from ..views.supermarket_view import *

urlpatterns =[
    re_path(r"categoy-detaile/(?P<slug>[-\w]+)/",Supermarket_detaile.as_view(),name="categoy-detaile"),
    path("category-grid/",SupermarketGrid.as_view(),name="category-grid"),
    path("category-supermarket/",SupermarketView.as_view(),name="category-supermarket"),
]
