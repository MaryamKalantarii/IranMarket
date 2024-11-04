from django import template
from product.models import *

register = template.Library()

@register.inclusion_tag("includes/similar-products.html")
def show_similar_products(product):
    clothing_categories = product.category_clothing.all()
    similar_clothings = Clothing.objects.filter(status=True, category_clothing__in=clothing_categories).order_by('-created_date')[:6]
    return {"similar_clothings": similar_clothings}

@register.inclusion_tag("includes/similar-diji.html")
def show_similar_diji(product):
    diji_categories = product.category_Dijitalgoods.all()
    similar_diji = Dijitalgoods.objects.filter(status=True, category_Dijitalgoods__in=diji_categories).order_by('-created_date')[:6]
    return {"similar_diji": similar_diji}

@register.inclusion_tag("includes/similar-home.html")
def show_similar_home(product):
    home_categories = product.category_Homeappliances.all()
    similar_home = Homeappliances.objects.filter(status=True, category_Homeappliances__in=home_categories).order_by('-created_date')[:6]
    return {"similar_home": similar_home}

@register.inclusion_tag("includes/similar-beauty.html")
def show_similar_beauty(product):
    beauty_categories = product.category_Beauty.all()
    similar_beauty = Beauty.objects.filter(status=True, category_Beauty__in=beauty_categories).order_by('-created_date')[:6]
    return {"similar_beauty": similar_beauty}
