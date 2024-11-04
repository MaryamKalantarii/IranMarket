from django.shortcuts import redirect
from django.views.generic import TemplateView,ListView,DetailView
from product.models import Beauty,Category_Beauty
from django.contrib import messages

class BeautyView(TemplateView):
    template_name = 'product/product_beauty/category_beauty.html'



class BeautyGrid(ListView):
    
    template_name = 'product/product_beauty/category-grid.html'
    
    def get_queryset(self):
        queryset = Beauty.objects.filter(status=True)


        # فیلتر بر اساس کتگوری
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category_Beauty__slug=category_slug)

        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category_Beauty.objects.all()  # ارسال لیست همه کتگوری‌ها به تمپلیت
        context['selected_category'] = self.request.GET.get('category')
        return context




class Beauty_detaile(DetailView):

    template_name = 'product/product_beauty/single-product.html'
    queryset = Beauty.objects.filter(status=True)

    def post(self, request, *args, **kwargs):
        messages.success(request, "محصول با موفقیت به سبد خرید اضافه شد.")
        return redirect(request.path_info)
   

