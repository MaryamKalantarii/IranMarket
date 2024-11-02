from django.urls import path,include,re_path
from ..views.beauty_view import *

urlpatterns =[
    re_path(r"categoy-detaile/(?P<slug>[-\w]+)/",Beauty_detaile.as_view(),name="categoy-detaile"),
    path("category-grid/",BeautyGrid.as_view(),name="category-grid"),
    path("category-beauty/",BeautyView.as_view(),name="category-beauty"),
]
