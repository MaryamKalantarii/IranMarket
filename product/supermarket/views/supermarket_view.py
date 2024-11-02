from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from product.models import Supermarket,Category_Supermarket


class SupermarketView(TemplateView):
    template_name = 'product/product_supermarket/category_supermarket.html'



class SupermarketGrid(ListView):
    
    template_name = 'product/product_supermarket/category-grid.html'
    
    def get_queryset(self):
        queryset = Supermarket.objects.filter(status=True)


        # فیلتر بر اساس کتگوری
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category_Supermarket__slug=category_slug)

        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category_Supermarket.objects.all()  # ارسال لیست همه کتگوری‌ها به تمپلیت
        context['selected_category'] = self.request.GET.get('category')
        return context




class Supermarket_detaile(DetailView):

    template_name = 'product/product_supermarket/single-product.html'
    queryset = Supermarket.objects.filter(status=True)
   

