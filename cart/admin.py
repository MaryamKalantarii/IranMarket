from django.contrib import admin
from .models import CartModel, CartItemModel
from .forms import CartItemAdminForm
@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


@admin.register(CartItemModel)
class CartItemModelAdmin(admin.ModelAdmin):
    form = CartItemAdminForm  # استفاده از فرم سفارشی
    list_display = ("id", "cart", "get_product_title", "quantity")

    def get_product_title(self, obj):
        """برگرداندن عنوان محصول"""
        if obj.product:
            return obj.product.title
        return "No Product"
    
    get_product_title.short_description = "Product Name"
