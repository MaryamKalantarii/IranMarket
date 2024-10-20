from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from product.models import Homeappliances,Category_Homeappliances


class HomeapplianceView(TemplateView):
    template_name = 'product/product_homeappliances/category_homeappliances.html'



class HomeapplianceGrid(ListView):
    
    template_name = 'product/product_homeappliances/category-grid.html'
    
    def get_queryset(self):
        queryset = Homeappliances.objects.filter(status=True)


        # فیلتر بر اساس کتگوری
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category_Homeappliances__slug=category_slug)

        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category_Homeappliances.objects.all()  # ارسال لیست همه کتگوری‌ها به تمپلیت
        context['selected_category'] = self.request.GET.get('category')
        return context




class homeappliances_detaile(DetailView):

    template_name = 'product/product_homeappliances/single-product.html'
    queryset = Homeappliances.objects.filter(status=True)
   

