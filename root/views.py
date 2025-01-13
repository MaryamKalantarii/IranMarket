from django.shortcuts import render
from django.views.generic import TemplateView
from django.apps import apps
from product.models import *
# Create your views here.



# class HomeView(TemplateView):
#     template_name = 'root/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         # دریافت مدل‌های خاص به صورت داینامیک
#         model_names = ['Clothing', 'Dijitalgoods','Homeappliances','Beauty','Appliances','Supermarket','Child_and_baby']
#         for model_name in model_names:
#             model = apps.get_model('product', model_name)
#             context[f'{model_name.lower()}_products'] = model.objects.filter(status=True)[:10]
        
#         return context



class HomeView(TemplateView):
    template_name = 'root/index.html'

    def get_context_data(self, **kwargs):
        # دریافت context پیش‌فرض
        context = super().get_context_data(**kwargs)
        
        # اضافه کردن داده‌های مدل‌ها به context
        context['clothing'] = Clothing.objects.filter(status=True)[:6]  # دریافت 10 محصول اول
        context['home'] = Homeappliances.objects.filter(status=True)[:6]  # دریافت 10 محصول اول
        
        return context
