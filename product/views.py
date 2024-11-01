from django.shortcuts import render
from django.db.models import Q
from .models import Clothing, Dijitalgoods, Homeappliances

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

        results += clothing_results + dijitalgoods_results + homeappliances_results

    return render(request, 'search/search.html', {'results': results})
