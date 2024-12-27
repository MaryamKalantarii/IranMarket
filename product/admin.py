from django.contrib import admin
from .models import *
from .forms import WishlistAdminForm
# Register your models here.
 

admin.site.register(Clothing)
admin.site.register(Dijitalgoods)
admin.site.register(Homeappliances)
admin.site.register(Beauty)
admin.site.register(Appliances)
admin.site.register(Supermarket)
admin.site.register(Child_and_baby)


admin.site.register(Category_clothing)
admin.site.register(Category_Dijitalgoods)
admin.site.register(Category_Homeappliances)
admin.site.register(Category_Beauty)
admin.site.register(Category_Appliances)
admin.site.register(Category_Supermarket)
admin.site.register(Category_Child_and_baby)

# @admin.register(WishlistProductModel)
# class WishlistProductModelAdmin(admin.ModelAdmin):
#     list_display = ("id", "user", "product")

@admin.register(WishlistProductModel)
class CartItemModelAdmin(admin.ModelAdmin):
    form = WishlistAdminForm  # استفاده از فرم سفارشی
    list_display = ("id", "user", "get_product_title")

    def get_product_title(self, obj):
        """برگرداندن عنوان محصول"""
        if obj.product:
            return obj.product.title
        return "No Product"
    
    get_product_title.short_description = "Product Name"
