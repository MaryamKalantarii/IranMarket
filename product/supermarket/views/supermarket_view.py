from django.shortcuts import redirect
from django.views.generic import TemplateView,ListView,DetailView
from product.models import Supermarket,Category_Supermarket,WishlistProductModel
from django.contrib import messages
from review.models import ReviewModel,ReviewStatusType
from django.contrib.contenttypes.models import ContentType

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

        # فیلتر بر اساس بازه‌ی قیمتی
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        # اعمال مرتب‌سازی بر اساس پارامتر sort
        sort_option = self.request.GET.get("sort")
          
        if sort_option == "cheapest":
            queryset = queryset.order_by('price')  
        elif sort_option == "most_expensive":
            queryset = queryset.order_by('-price')  
        elif sort_option == "newest":
            queryset = queryset.order_by('-created_date')  
        elif sort_option == "oldest":
            queryset = queryset.order_by('created_date')  
    
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category_Supermarket.objects.all()  # ارسال لیست همه کتگوری‌ها به تمپلیت
        context['selected_category'] = self.request.GET.get('category')
        return context




class Supermarket_detaile(DetailView):

    template_name = 'product/product_supermarket/single-product.html'
    queryset = Supermarket.objects.filter(status=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product= self.get_object()
        context['model_name'] = product._meta.model_name  
        user = self.request.user

            # دریافت کامنت‌های تأیید شده
        accepted_reviews = ReviewModel.objects.filter(
            product_content_type=ContentType.objects.get_for_model(product),
            product_object_id=product.id,
            status=ReviewStatusType.accepted.value  # فقط کامنت‌های تأیید شده
        )
        
        context['reviews'] = accepted_reviews
       
        if user.is_authenticated:
            wishlist_items = WishlistProductModel.objects.filter(user=user)
            wishlist_ids = set(
                (item.content_type_id, item.object_id) for item in wishlist_items
            )
            product = self.get_object()
            is_in_wishlist = (
                ContentType.objects.get_for_model(product).id, product.id
            ) in wishlist_ids
            context['is_in_wishlist'] = is_in_wishlist
        else:
            context['is_in_wishlist'] = False  
        
        return context
    def post(self, request, *args, **kwargs):
        messages.success(request, "محصول با موفقیت به سبد خرید اضافه شد.")
        return redirect(request.path_info)
   

