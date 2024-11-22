from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

class OrderStatusType(models.IntegerChoices):
    pending = 1 , "در انتظار پرداخت"
    success = 2, "موفقیت آمیز"
    failed = 3,"لغو شده"

class UserAddressModel(models.Model):
    user = models.ForeignKey('accounts.CustomeUser',on_delete=models.CASCADE)
    
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class CouponModel(models.Model):
    code = models.CharField(max_length=100)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    max_limit_usage = models.PositiveIntegerField(default=10)
    used_by = models.ManyToManyField('accounts.CustomeUser',related_name = "coupon_users",blank=True)
    
    expiration_date = models.DateTimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


# Create your models here.
class OrderModel(models.Model):
    user = models.ForeignKey('accounts.CustomeUser',on_delete=models.PROTECT)
    
    # order address information
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    
    total_price = models.DecimalField(default=0,max_digits=10,decimal_places=0)

    coupon = models.ForeignKey(CouponModel,on_delete=models.PROTECT,null=True,blank=True)
    status = models.IntegerField(choices=OrderStatusType.choices,default=OrderStatusType.pending.value)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
    
    def calculate_total_price(self):
        return sum(item.price * item.quantity for item in self.order_items.all())
    
    def __str__(self):
        return f"{self.user.email} - {self.id}"
    
    def get_status(self):
        return {
            "id":self.status,
            "title":OrderStatusType(self.status).name,
            "label":OrderStatusType(self.status).label,
        }
        
    def get_full_address(self):
        return f"{self.state},{self.city},{self.address}"
    
    @property
    def is_successful(self):
        return self.status == OrderStatusType.success.value
    
    def get_price(self):
        
        if self.coupon:            
            return round(self.total_price - (self.total_price * Decimal( self.coupon.discount_percent /100)))
        else:
            return self.total_price
    
    
class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel,on_delete=models.CASCADE,related_name="order_items") 
    product_content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    product_object_id = models.PositiveIntegerField()
    product = GenericForeignKey('product_content_type', 'product_object_id')
    quantity = models.PositiveIntegerField(default=0)

    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.product.title} - {self.order.id}"
    