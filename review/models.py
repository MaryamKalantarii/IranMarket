from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class ReviewStatusType(models.IntegerChoices):
    pending = 1, "در انتظار تایید"
    accepted = 2, "تایید شده"
    rejected = 3, "رد شده"


class ReviewModel(models.Model):
    user = models.ForeignKey('accounts.CustomeUser', on_delete=models.CASCADE)
    product_content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    product_object_id = models.PositiveIntegerField()
    product = GenericForeignKey('product_content_type', 'product_object_id')
    description = models.TextField()
    status = models.IntegerField(
        choices=ReviewStatusType.choices, default=ReviewStatusType.pending.value)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]
    
    def __str__(self):
        return f"{self.user} - {self.product.id}"
    
    
    def get_status(self):
        return {
            "id":self.status,
            "title":ReviewStatusType(self.status).name,
            "label":ReviewStatusType(self.status).label,
        }
        