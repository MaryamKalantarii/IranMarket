from django.urls import path,include,re_path
from ..views.clothingviews import *

urlpatterns =[
    re_path(r"categoy-detaile/(?P<slug>[-\w]+)/",Clothing_detaile.as_view(),name="categoy-detaile"),
    path("category-grid/",ClothingGrid.as_view(),name="category-grid"),
    path("category-clothing/",ClothingView.as_view(),name="category-clothing"),
]
