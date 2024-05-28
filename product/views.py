from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ProductView(TemplateView):
    template_name = 'product/category.html'



class Product_index_View(TemplateView):
    template_name = 'product/category-index.html'



class Product_single_View(TemplateView):
    template_name = 'product/single-product.html'
