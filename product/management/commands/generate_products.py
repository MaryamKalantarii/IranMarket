import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from product.models import Clothing, Category_clothing, Category_color
from pathlib import Path
from django.core.files import File
 
BASE_DIR = Path(__file__).resolve().parent



class Command(BaseCommand):
    help = 'Generate fake products'

    def handle(self, *args, **options):
        fake = Faker(locale="fa_IR")
        
        # List of image paths relative to BASE_DIR
        image_list = [
            "./images/1.jpg",
            "./images/2.jpg",
            "./images/3.jpg",
            "./images/4.jpg",
            "./images/5.jpg",
            "./images/6.jpg",
            "./images/7.jpg",
            "./images/8.jpg",
            "./images/9.jpg",
            "./images/10.jpg",
            "./images/11.jpg",
            "./images/12.jpg",
            "./images/13.jpg",
            "./images/14.jpg",
            "./images/15.jpg",
            "./images/16.jpg",
            "./images/17.jpg",
            "./images/18.jpg",
            
            # Add more images if necessary
        ]

        categories = Category_clothing.objects.all()
        categories_color = Category_color.objects.all()

        for _ in range(10):  # Adjust the range for the number of records you want to create
            num_categories = random.randint(1, 2)
            num_categories_color = random.randint(1, 2)  # Added this for color categories
            category_clothing = random.sample(list(categories), num_categories)
            category_color = random.sample(list(categories_color), num_categories_color)

            title = fake.word()  # Remove the comma to prevent tuple creation
            content1 = fake.text()
            content2 = fake.text()
            content3 = fake.text()
            content4 = fake.text()
            content5 = fake.text()

            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image, "rb"), name=Path(selected_image).name)
            slug = slugify(title, allow_unicode=True)  # Remove the comma to prevent tuple creation
            more_details = fake.text()
            size = random.choice(['S', 'M', 'L', 'XL'])
            status = True  # You can randomize this if needed
            
            # Creating the product
            product = Clothing.objects.create(
                title=title,
                slug=slug,
                image1=image_obj,
                more_details=more_details,
                size=size,
                status=status,
                content1=content1,
                content2=content2,
                content3=content3,
                content4=content4,
                content5=content5,
            )

            # Setting category fields
            product.category_clothing.set(category_clothing)
            product.category_color.set(category_color)

        self.stdout.write(self.style.SUCCESS('Successfully generated 10 fake products.'))

