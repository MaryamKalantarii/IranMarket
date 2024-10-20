from product.models import *


def categories_processor(request):
    category_clothing = Category_clothing.objects.all()
    category_dijitalgoods = Category_Dijitalgoods.objects.all()
    category_homeappliances = Category_Homeappliances.objects.all()
    category_beauty = Category_Beauty.objects.all()
    

    return {
        'categories': category_clothing,
        'category_dijitalgoods': category_dijitalgoods,
        'category_homeappliances': category_homeappliances,
        'category_beauty': category_beauty,
        'category_appliances': Category_Appliances.objects.all(),
        'category_supermarket': Category_Supermarket.objects.all(),
        'category_child': Category_Child_and_baby.objects.all(),
    }
