from django.shortcuts import render
from django.views.generic import TemplateView
from django.apps import apps
from product.models import *
# Create your views here.


class HomeView(TemplateView):
    template_name = 'root/index.html'

    def get_context_data(self, **kwargs):
        # دریافت context پیش‌فرض
        context = super().get_context_data(**kwargs)
        
        # اضافه کردن داده‌های مدل‌ها به context
        context['clothing'] = Clothing.objects.filter(status=True)[:6]  # دریافت 10 محصول اول
        context['home'] = Homeappliances.objects.filter(status=True)[:6]
        context['beauty'] = Beauty.objects.filter(status=True)[:6]
        context['dijitalgoods'] = Dijitalgoods.objects.filter(status=True)[:6]
        context['child'] = Child_and_baby.objects.filter(status=True)[:6]
        
        return context


class AboutView(TemplateView):
    template_name = 'root/about.html'

class FaqView(TemplateView):
    template_name = 'root/faq.html'