import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from product.models import *
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
         # Generate fake data for Clothing model
        self.generate_fake_clothing(fake, image_list)
        # Generate fake data for DigitalGoods model
        self.generate_fake_digital_goods(fake, image_list)
        self.generate_fake_Homeappliances(fake,image_list)
        self.generate_fake_Beauty(fake, image_list)
        self.generate_fake_Appliances(fake, image_list)
        self.generate_fake_Supermarket(fake, image_list)
        self.generate_fake_Child_and_baby(fake, image_list)


        self.stdout.write(self.style.SUCCESS('Successfully generated fake products for multiple models.'))
    def generate_fake_clothing(self, fake, image_list):
        categories = Category_clothing.objects.all()

        for _ in range(10):  # Adjust the range as needed
            num_categories = random.randint(1, 2)
            category_clothing = random.sample(list(categories), num_categories)

            title = fake.word()
            description = fake.text()
            brief_description = fake.text()

            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image, "rb"), name=Path(selected_image).name)
            slug = slugify(title, allow_unicode=True)
            # Ensure unique slug
            base_slug = slug
            counter = 1
            while Clothing.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            size = random.choice(['S', 'M', 'L', 'XL'])
            price = fake.random_int(min=10000, max=100000)
            discount_percent = fake.random_int(min=0, max=50)
            stock = fake.random_int(min=0, max=10)
            status = True

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

    def generate_fake_digital_goods(self, fake, image_list):
        categories =Category_Dijitalgoods.objects.all()

        for _ in range(10):  # Adjust the range as needed
            num_categories = random.randint(1, 2)
            category_Dijitalgoods = random.sample(list(categories), num_categories)

            title = fake.word()
            description = fake.text()
            brief_description = fake.text()

            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image, "rb"), name=Path(selected_image).name)
            slug = slugify(title, allow_unicode=True)
            # Ensure unique slug
            base_slug = slug
            counter = 1
            while Dijitalgoods.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            warranty = random.choice(['یک ماه', 'دو ماه', 'سه ماه', 'چهار ماه'])
            price = fake.random_int(min=10000, max=100000)
            discount_percent = fake.random_int(min=0, max=50)
            stock = fake.random_int(min=0, max=10)
            status = True

            # Creating the product
            product = Dijitalgoods.objects.create(
                title=title,
                description=description,
                brief_description=brief_description,
                slug=slug,
                image1=image_obj,
                warranty=warranty,
                stock=stock,
                price=price,
                discount_percent=discount_percent,
                status=status,
            )

            # Setting category fields
            product.category_Dijitalgoods.set(category_Dijitalgoods)
    def generate_fake_Homeappliances(self, fake, image_list):
        categories =Category_Homeappliances.objects.all()

        for _ in range(10):  # Adjust the range as needed
            num_categories = random.randint(1, 2)
            category_Homeappliances = random.sample(list(categories), num_categories)

            title = fake.word()
            description = fake.text()
            brief_description = fake.text()

            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image, "rb"), name=Path(selected_image).name)
            slug = slugify(title, allow_unicode=True)
            # Ensure unique slug
            base_slug = slug
            counter = 1
            while Homeappliances.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            warranty = random.choice(['یک ماه', 'دو ماه', 'سه ماه', 'چهار ماه'])
            price = fake.random_int(min=10000, max=100000)
            discount_percent = fake.random_int(min=0, max=50)
            stock = fake.random_int(min=0, max=10)
            status = True

            # Creating the product
            product = Homeappliances.objects.create(
                title=title,
                description=description,
                brief_description=brief_description,
                slug=slug,
                image1=image_obj,
                warranty=warranty,
                stock=stock,
                price=price,
                discount_percent=discount_percent,
                status=status,
            )

            # Setting category fields
            product.category_Homeappliances.set(category_Homeappliances)
    def generate_fake_Beauty(self, fake, image_list):
        categories = Category_Beauty.objects.all()

        for _ in range(10):  # Adjust the range as needed
            num_categories = random.randint(1, 2)
            category_Beauty = random.sample(list(categories), num_categories)

            title = fake.word()
            description = fake.text()
            brief_description = fake.text()

            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image, "rb"), name=Path(selected_image).name)
            slug = slugify(title, allow_unicode=True)
            # Ensure unique slug
            base_slug = slug
            counter = 1
            while Beauty.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            price = fake.random_int(min=10000, max=100000)
            discount_percent = fake.random_int(min=0, max=50)
            stock = fake.random_int(min=0, max=100)
            exception_date = random.choice(['یک ماه', 'دو ماه', 'سه ماه', 'چهار ماه'])
            status = True
            # Creating the product
            product = Beauty.objects.create(
                title=title,
                description=description,
                brief_description=brief_description,
                slug=slug,
                stock=stock,
                image1=image_obj,
                price=price,
                discount_percent=discount_percent,
                exception_date = exception_date,
                status=status,
            )

            # Setting category fields
            product.category_Beauty.set(category_Beauty)
    def generate_fake_Appliances(self, fake, image_list):
        categories = Category_Appliances.objects.all()

        for _ in range(10):  # Adjust the range as needed
            num_categories = random.randint(1, 2)
            category_Appliances = random.sample(list(categories), num_categories)

            title = fake.word()
            description = fake.text()
            brief_description = fake.text()

            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image, "rb"), name=Path(selected_image).name)
            slug = slugify(title, allow_unicode=True)
            # Ensure unique slug
            base_slug = slug
            counter = 1
            while Appliances.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            price = fake.random_int(min=10000, max=100000)
            discount_percent = fake.random_int(min=0, max=50)
            stock = fake.random_int(min=0 , max=100)
            warranty = random.choice(['یک ماه', 'دو ماه', 'سه ماه', 'چهار ماه'])

            status = True
            # Creating the product
            product = Appliances.objects.create(
                title=title,
                description=description,
                brief_description=brief_description,
                slug=slug,
                image1=image_obj,
                price=price,
                stock = stock,
                warranty=warranty,
                discount_percent=discount_percent,
                status=status,
            )

            # Setting category fields
            product.category_Appliances.set(category_Appliances)
    def generate_fake_Supermarket(self, fake, image_list):
        categories = Category_Supermarket.objects.all()

        for _ in range(10):  # Adjust the range as needed
            num_categories = random.randint(1, 2)
            category_Supermarket = random.sample(list(categories), num_categories)

            title = fake.word()
            description = fake.text()
            brief_description = fake.text()

            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image, "rb"), name=Path(selected_image).name)
            slug = slugify(title, allow_unicode=True)
            # Ensure unique slug
            base_slug = slug
            counter = 1
            while Supermarket.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            price = fake.random_int(min=10000, max=100000)
            discount_percent = fake.random_int(min=0, max=50)
            stock = fake.random_int(min=0, max=100)
            exception_date = random.choice(['یک ماه', 'دو ماه', 'سه ماه', 'چهار ماه'])

            status = True
            # Creating the product
            product = Supermarket.objects.create(
                title=title,
                description=description,
                brief_description=brief_description,
                slug=slug,
                image1=image_obj,
                price=price,
                stock=stock,
                discount_percent=discount_percent,
                status=status,
                exception_date=exception_date,
            )

            # Setting category fields
            product.category_Supermarket.set(category_Supermarket)
    def generate_fake_Child_and_baby(self, fake, image_list):
        categories = Category_Child_and_baby.objects.all()

        for _ in range(10):  # Adjust the range as needed
            num_categories = random.randint(1, 2)
            category_Child_and_baby = random.sample(list(categories), num_categories)

            title = fake.word()
            description = fake.text()
            brief_description = fake.text()

            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image, "rb"), name=Path(selected_image).name)
            slug = slugify(title, allow_unicode=True)
            # Ensure unique slug
            base_slug = slug
            counter = 1
            while Child_and_baby.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            size = random.choice(['S', 'M', 'L', 'XL'])
            price = fake.random_int(min=10000, max=100000)
            discount_percent = fake.random_int(min=0, max=50)
            stock = fake.random_int(min=0, max=10)
            status = True

            # Creating the product
            product = Child_and_baby.objects.create(
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
            product.category_Child_and_baby.set(category_Child_and_baby)
