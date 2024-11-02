from django.shortcuts import render
from django.db.models import Q
from .models import *

def search_products(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        clothing_results = list(Clothing.objects.filter(
            Q(title__icontains=query) | Q(brief_description__icontains=query)
        ).prefetch_related('category_clothing').distinct())
        for item in clothing_results:
            item.product_type = "Clothing"
            item.namespace = "product:clothing:categoy-detaile"

        dijitalgoods_results = list(Dijitalgoods.objects.filter(
            Q(title__icontains=query) | Q(brief_description__icontains=query)
        ).prefetch_related('category_Dijitalgoods').distinct())
        for item in dijitalgoods_results:
            item.product_type = "Dijitalgoods"
            item.namespace = "product:dijitalgoods:categoy-detaile"

        homeappliances_results = list(Homeappliances.objects.filter(
            Q(title__icontains=query) | Q(brief_description__icontains=query)
        ).prefetch_related('category_Homeappliances').distinct())
        for item in homeappliances_results:
            item.product_type = "Homeappliances"
            item.namespace = "product:homeappliances:categoy-detaile"

        beauty_results = list(Beauty.objects.filter(
            Q(title__icontains=query) | Q(brief_description__icontains=query)
        ).prefetch_related('category_Beauty').distinct())
        for item in beauty_results:
            item.product_type = "Beauty"
            item.namespace = "product:beauty:categoy-detaile"


        appliances_results = list(Appliances.objects.filter(
            Q(title__icontains=query) | Q(brief_description__icontains=query)
        ).prefetch_related('category_Appliances').distinct())
        for item in appliances_results:
            item.product_type = "Appliances"
            item.namespace = "product:appliances:categoy-detaile"
        

        supermarket_results = list(Supermarket.objects.filter(
            Q(title__icontains=query) | Q(brief_description__icontains=query)
        ).prefetch_related('category_Supermarket').distinct())
        for item in supermarket_results:
            item.product_type = "Supermarket"
            item.namespace = "product:supermarket:categoy-detaile"
        
        Child_and_baby_results = list(Child_and_baby.objects.filter(
            Q(title__icontains=query) | Q(brief_description__icontains=query)
        ).prefetch_related('category_Child_and_baby').distinct())
        for item in Child_and_baby_results:
            item.product_type = "Child_and_baby"
            item.namespace = "product:child:categoy-detaile"

        results += clothing_results + dijitalgoods_results + homeappliances_results + beauty_results + appliances_results + supermarket_results + Child_and_baby_results 

    return render(request, 'search/search.html', {'results': results})
