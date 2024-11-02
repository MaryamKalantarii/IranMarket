from django.urls import path,include,re_path
from ..views.child_view import *

urlpatterns =[
    re_path(r"categoy-detaile/(?P<slug>[-\w]+)/",Child_detaile.as_view(),name="categoy-detaile"),
    path("category-grid/",ChildGrid.as_view(),name="category-grid"),
    path("category-child/",ChildView.as_view(),name="category-child"),
]
