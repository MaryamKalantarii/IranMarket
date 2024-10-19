from product.models import *

def categories_processor(request):
    categories = Category_clothing.objects.all()  # تمام کتگوری‌ها را دریافت می‌کنیم
    return {'categories': categories}  # به تمام تمپلیت‌ها ارسال می‌شود

