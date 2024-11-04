from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from product.models import Dijitalgoods , Category_Dijitalgoods
from django.contrib import messages

class DijitalgoodsView(TemplateView):
    template_name = 'product/product_dijitalgoods/category_dijitalgoods.html'



class DijitalgoodsGrid(ListView):
    
    template_name = 'product/product_dijitalgoods/category-grid.html'
    
    def get_queryset(self):
        queryset = Dijitalgoods.objects.filter(status=True)

   
        # فیلتر بر اساس کتگوری
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category_Dijitalgoods__slug=category_slug)

        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_dijitalgoods'] = Category_Dijitalgoods.objects.all()  # ارسال لیست همه کتگوری‌ها به تمپلیت
        context['selected_category'] = self.request.GET.get('category')
        return context




class Dijitalgoods_detaile(DetailView):

    template_name = 'product/product_dijitalgoods/single-product.html'
    queryset = Dijitalgoods.objects.filter(status=True)

    def post(self, request, *args, **kwargs):
        messages.success(request, "محصول با موفقیت به سبد خرید اضافه شد.")
        return redirect(request.path_info)