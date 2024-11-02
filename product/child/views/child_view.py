from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from product.models import Child_and_baby,Category_Child_and_baby


class ChildView(TemplateView):
    template_name = 'product/product_child/category_child.html'



class ChildGrid(ListView):
    
    template_name = 'product/product_child/category-grid.html'
    
    def get_queryset(self):
        queryset = Child_and_baby.objects.filter(status=True)

        # فیلتر بر اساس کتگوری
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category_Child_and_baby__slug=category_slug)

        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category_Child_and_baby.objects.all()  # ارسال لیست همه کتگوری‌ها به تمپلیت
        context['selected_category'] = self.request.GET.get('category')
        return context




class Child_detaile(DetailView):

    template_name = 'product/product_child/single-product.html'
    queryset = Child_and_baby.objects.filter(status=True)
   

