from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from product.models import Clothing,Category_clothing
from django.contrib import messages

class ClothingView(TemplateView):
    template_name = 'product/product_clothing/category_clothing.html'




class ClothingGrid(ListView):
    template_name = 'product/product_clothing/category-grid.html'
    context_object_name = 'clothing_items'

    def get_queryset(self):
        queryset = Clothing.objects.filter(status=True)
        
        # فیلتر بر اساس کتگوری
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category_clothing__slug=category_slug)
        
        # فیلتر بر اساس بازه‌ی قیمتی
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        return queryset

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category_clothing.objects.all()  # ارسال لیست همه کتگوری‌ها به تمپلیت
        context['selected_category'] = self.request.GET.get('category')
        return context





class Clothing_detaile(DetailView):
    template_name = 'product/product_clothing/single-product.html'
    queryset = Clothing.objects.filter(status=True)

    def post(self, request, *args, **kwargs):
        messages.success(request, "محصول با موفقیت به سبد خرید اضافه شد.")
        return redirect(request.path_info)