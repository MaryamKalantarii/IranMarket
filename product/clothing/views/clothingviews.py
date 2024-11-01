from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from product.models import Clothing,Category_clothing


class ClothingView(TemplateView):
    template_name = 'product/product_clothing/category_clothing.html'



class ClothingGrid(ListView):
    
    template_name = 'product/product_clothing/category-grid.html'
    
    def get_queryset(self):
        queryset = Clothing.objects.filter(status=True)

    
        # فیلتر بر اساس کتگوری
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category_clothing__slug=category_slug)

        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category_clothing.objects.all()  # ارسال لیست همه کتگوری‌ها به تمپلیت
        context['selected_category'] = self.request.GET.get('category')
        return context




class Clothing_detaile(DetailView):

    template_name = 'product/product_clothing/single-product.html'
    queryset = Clothing.objects.filter(status=True)
   

