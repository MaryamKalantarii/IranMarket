from django import template
from product.models import *

register = template.Library()

@register.inclusion_tag("includes/similar-products.html")
def show_similar_products(product):
    clothing_categories = product.category_clothing.all()
    similar_clothings = Clothing.objects.filter(status=True, category_clothing__in=clothing_categories).distinct().order_by('-created_date')[:6]
    return {"similar_clothings": similar_clothings}

@register.inclusion_tag("includes/similar-diji.html")
def show_similar_diji(product):
    diji_categories = product.category_Dijitalgoods.all()
    similar_diji = Dijitalgoods.objects.filter(status=True, category_Dijitalgoods__in=diji_categories).distinct().order_by('-created_date')[:6]
    return {"similar_diji": similar_diji}

@register.inclusion_tag("includes/similar-home.html")
def show_similar_home(product):
    home_categories = product.category_Homeappliances.all()
    similar_home = Homeappliances.objects.filter(status=True, category_Homeappliances__in=home_categories).distinct().order_by('-created_date')[:6]
    return {"similar_home": similar_home}

@register.inclusion_tag("includes/similar-beauty.html")
def show_similar_beauty(product):
    beauty_categories = product.category_Beauty.all()
    similar_beauty = Beauty.objects.filter(status=True, category_Beauty__in=beauty_categories).distinct().order_by('-created_date')[:6]
    return {"similar_beauty": similar_beauty}

@register.inclusion_tag("includes/similar-app.html")
def show_similar_app(product):
    app_categories = product.category_Appliances.all()
    similar_app = Appliances.objects.filter(status=True, category_Appliances__in=app_categories).distinct().order_by('-created_date')[:6]
    return {"similar_app": similar_app}

@register.inclusion_tag("includes/similar-supermarket.html")
def show_similar_supermarket(product):
    supermarket_categories = product.category_Supermarket.all()
    similar_supermarket = Supermarket.objects.filter(status=True, category_Supermarket__in=supermarket_categories).distinct().order_by('-created_date')[:6]
    return {"similar_supermarket": similar_supermarket}

@register.inclusion_tag("includes/similar-child.html")
def show_similar_child(product):
    child_categories = product.category_Child_and_baby.all()
    similar_child = Child_and_baby.objects.filter(status=True, category_Child_and_baby__in=child_categories).distinct().order_by('-created_date')[:6]
    return {"similar_child": similar_child}