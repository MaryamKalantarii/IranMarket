from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ClothingView(TemplateView):
    template_name = 'product/category_clothing.html'


class DijitalgoodsView(TemplateView):
    template_name = 'product/category_Dijitalgoods.html'


class HomeappliancesView(TemplateView):
    template_name = 'product/category_Homeappliances.html'











class Product_single_View(TemplateView):
    template_name = 'product/single-product.html'
