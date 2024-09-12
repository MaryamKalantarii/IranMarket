from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from product.models import *
# Create your views here.

class ClothingView(TemplateView):
    template_name = 'product/product_clothing/category_clothing.html'


# class ClothingGrid(TemplateView):
#     template_name = 'product/product_clothing/category.html'




class ClothingGrid(ListView):
    model = Clothing
    template_name = 'product/product_clothing/category-grid.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        # دریافت پارامتر جستجو
        search_q = self.request.GET.get("q")
        if search_q:
            queryset = queryset.filter(title__icontains=search_q)

        # فیلتر بر اساس کتگوری
        category_slug = self.request.GET.get("category")
        print(f"Category slug: {category_slug}")
        if category_slug:
            queryset = queryset.filter(category_clothing__slug=category_slug)
       
    
        return queryset




class Clothing_detaile(TemplateView):
    template_name = 'product/product_clothing/single-product.html'



#########################

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
