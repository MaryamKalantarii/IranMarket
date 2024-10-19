# from django.core.management.base import BaseCommand
# from faker import Faker
# from product.models import Category_clothing
# from django.utils.text import slugify


# class Command(BaseCommand): 
#     help = 'Generate fake categories'

#     def handle(self, *args, **options):
#         fake = Faker(locale="fa_IR")

#         for _ in range(10):
            
#             name = fake.word()
#             slug = slugify(name, allow_unicode=True)
#             Category_clothing.objects.get_or_create(name=name, slug=slug)
#         self.stdout.write(self.style.SUCCESS('Successfully generated 10 fake categories'))

from django.core.management.base import BaseCommand
from faker import Faker
from django.utils.text import slugify
from django.apps import apps


class Command(BaseCommand):
    help = 'Generate fake categories for all category models'

    def handle(self, *args, **options):
        fake = Faker(locale="fa_IR")

        # لیستی از نام مدل‌های دسته‌بندی که می‌خواهید برای آن‌ها داده فیک تولید کنید
        category_models = [
            'Category_clothing',
            'Category_Dijitalgoods',
            # مدل‌های دیگر را اینجا اضافه کنید
        ]

        for model_name in category_models:
            # دریافت مدل بر اساس نام
            model = apps.get_model('product', model_name)

            for _ in range(10):
                name = fake.word()
                slug = slugify(name, allow_unicode=True)
                # ایجاد یا دریافت دسته‌بندی فیک
                model.objects.get_or_create(name=name, slug=slug)

            self.stdout.write(self.style.SUCCESS(f'Successfully generated 10 fake categories for {model_name}'))
