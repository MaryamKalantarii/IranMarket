from django.urls import path,include,re_path
from ..views.dijitalgoods_views import *

urlpatterns =[
    re_path(r"categoy-detaile/(?P<slug>[-\w]+)/",Dijitalgoods_detaile.as_view,name="categoy-detaile"),
    path("category-grid/",DijitalgoodsGrid.as_view(),name="category-grid"),
    path("category-dijitalgoods/",DijitalgoodsView.as_view(),name="category-dijitalgoods"),
]
