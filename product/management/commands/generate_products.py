import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from product.models import Clothing, Category_clothing
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
        

        for _ in range(10):  # Adjust the range for the number of records you want to create
            num_categories = random.randint(1, 2)
            category_clothing = random.sample(list(categories), num_categories)

            title = fake.word()  # Remove the comma to prevent tuple creation
            description = fake.text()
            brief_description = fake.text()
            

            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image, "rb"), name=Path(selected_image).name)
            slug = slugify(title, allow_unicode=True)  # Remove the comma to prevent tuple creation
            size = random.choice(['S', 'M', 'L', 'XL'])
            price = fake.random_int(min=10000, max=100000)
            discount_percent = fake.random_int(min=0, max=50)
            stock = fake.random_int(min=0, max=10)
            status = True  # You can randomize this if needed
            
            # Creating the product
            product = Clothing.objects.create(
                title=title,
                description=description,
                brief_description=brief_description,
                slug=slug,
                image1=image_obj,
                size=size,
                stock=stock,
                price=price,
                discount_percent=discount_percent,
                status=status,
                
            )

            # Setting category fields
            product.category_clothing.set(category_clothing)
            

        self.stdout.write(self.style.SUCCESS('Successfully generated 10 fake products.'))

