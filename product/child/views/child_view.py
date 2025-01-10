from django.shortcuts import redirect
from django.views.generic import TemplateView,ListView,DetailView
from product.models import Child_and_baby,Category_Child_and_baby,WishlistProductModel
from django.contrib import messages
from review.models import ReviewModel,ReviewStatusType
from django.contrib.contenttypes.models import ContentType

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
   

