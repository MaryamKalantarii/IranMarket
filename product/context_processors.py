from product.models import *

# def categories_processor(request):
#     categories = Category_clothing.objects.all()  # تمام کتگوری‌ها را دریافت می‌کنیم
#     return {'categories': categories}  # به تمام تمپلیت‌ها ارسال می‌شود


# def dijitalgoods_processor(request):
#     category_dijitalgoods = Category_Dijitalgoods.objects.all()  
#     return {'category_dijitalgoods': category_dijitalgoods}  



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
