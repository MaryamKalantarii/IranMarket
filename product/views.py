from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ClothingView(TemplateView):
    template_name = 'product/product_clothing/category_clothing.html'


class DijitalgoodsView(TemplateView):
    template_name = 'product/product_dijitalgoods/category_Dijitalgoods.html'


class HomeappliancesView(TemplateView):
    template_name = 'product/product_homeappliances/category_Homeappliances.html'


class BeautyView(TemplateView):
    template_name = 'product/category_Beauty.html'


class AppliancesView(TemplateView):
    template_name = 'product/category_Appliances.html'


class SupermarketView(TemplateView):
    template_name = 'product/category_Supermarket.html'


class Child_and_babyView(TemplateView):
    template_name = 'product/category_Child_and_baby.html'




class Product_single_View(TemplateView):
    template_name = 'product/single-product.html'
