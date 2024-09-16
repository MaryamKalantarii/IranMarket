from django import template
from product.models import *

register = template.Library()

@register.inclusion_tag("includes/similar-products.html")
def show_similar_products(product):
    clothing_categories = product.category_clothing.all()
    similar_clothings = Clothing.objects.filter(status=True,category_clothing__in=clothing_categories).order_by('-created_date')[:6]
    return {"similar_clothings": similar_clothings}