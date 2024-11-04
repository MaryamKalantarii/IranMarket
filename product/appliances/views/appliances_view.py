from django.shortcuts import redirect
from django.views.generic import TemplateView,ListView,DetailView
from product.models import Appliances,Category_Appliances
from django.contrib import messages

class AppliancesView(TemplateView):
    template_name = 'product/product_appliances/category_appliances.html'



class AppliancesGrid(ListView):
    
    template_name = 'product/product_appliances/category-grid.html'
    
    def get_queryset(self):
        queryset = Appliances.objects.filter(status=True)

    

        # فیلتر بر اساس کتگوری
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category_Appliances__slug=category_slug)

        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category_Appliances.objects.all()  # ارسال لیست همه کتگوری‌ها به تمپلیت
        context['selected_category'] = self.request.GET.get('category')
        return context




class Appliances_detaile(DetailView):

    template_name = 'product/product_appliances/single-product.html'
    queryset = Appliances.objects.filter(status=True)

    def post(self, request, *args, **kwargs):
        messages.success(request, "محصول با موفقیت به سبد خرید اضافه شد.")
        return redirect(request.path_info)
   

