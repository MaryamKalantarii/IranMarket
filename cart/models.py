from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomeUser
# Create your models here.

class CartModel(models.Model):
    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    
    def calculate_total_price(self):
        return sum(item.product.get_price() * item.quantity for item in self.cart_items.all())
    
class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, related_name="cart_items")
    
    # استفاده از ContentType برای نگه داشتن نوع مدل محصول
    product_content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    
    # نگه داشتن ID محصول
    product_object_id = models.PositiveIntegerField()
    
    # ایجاد GenericForeignKey با استفاده از دو فیلد بالا
    product = GenericForeignKey('product_content_type', 'product_object_id')
    
    quantity = models.PositiveIntegerField(default=0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.title}-{self.cart.id}"