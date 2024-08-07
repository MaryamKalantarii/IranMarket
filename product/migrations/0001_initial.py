# Generated by Django 5.0.6 on 2024-08-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Appliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category_Beauty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='Brandimage')),
            ],
        ),
        migrations.CreateModel(
            name='Category_Child_and_baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category_clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='colors')),
            ],
        ),
        migrations.CreateModel(
            name='Category_Dijitalgoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category_Homeappliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category_Supermarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Beauty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content1', models.CharField(max_length=255)),
                ('content2', models.CharField(blank=True, max_length=100, null=True)),
                ('content3', models.CharField(blank=True, max_length=255, null=True)),
                ('content4', models.CharField(blank=True, max_length=255, null=True)),
                ('content5', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.ImageField(upload_to='beauty')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='beauty')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='beauty')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='beauty')),
                ('more_details', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('off', models.IntegerField(blank=True, null=True)),
                ('exception_date', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('amazing_offer', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category_Beauty', models.ManyToManyField(to='product.category_beauty')),
                ('category_brand', models.ManyToManyField(to='product.category_brand')),
                ('category_color', models.ManyToManyField(to='product.category_color')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Appliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content1', models.CharField(max_length=255)),
                ('content2', models.CharField(blank=True, max_length=100, null=True)),
                ('content3', models.CharField(blank=True, max_length=255, null=True)),
                ('content4', models.CharField(blank=True, max_length=255, null=True)),
                ('content5', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.ImageField(upload_to='appliances')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='appliances')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='appliances')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='appliances')),
                ('more_details', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('off', models.IntegerField(blank=True, null=True)),
                ('warranty', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('amazing_offer', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category_Appliances', models.ManyToManyField(to='product.category_appliances')),
                ('category_brand', models.ManyToManyField(to='product.category_brand')),
                ('category_color', models.ManyToManyField(to='product.category_color')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Child_and_baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content1', models.CharField(max_length=255)),
                ('content2', models.CharField(blank=True, max_length=100, null=True)),
                ('content3', models.CharField(blank=True, max_length=255, null=True)),
                ('content4', models.CharField(blank=True, max_length=255, null=True)),
                ('content5', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.ImageField(upload_to='child_and_baby')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='child_and_baby')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='child_and_baby')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='child_and_baby')),
                ('more_details', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('off', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('amazing_offer', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category_Child_and_baby', models.ManyToManyField(to='product.category_child_and_baby')),
                ('category_color', models.ManyToManyField(to='product.category_color')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content1', models.CharField(max_length=255)),
                ('content2', models.CharField(blank=True, max_length=100, null=True)),
                ('content3', models.CharField(blank=True, max_length=255, null=True)),
                ('content4', models.CharField(blank=True, max_length=255, null=True)),
                ('content5', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.ImageField(upload_to='clothings')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='clothings')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='clothings')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='clothings')),
                ('more_details', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('off', models.IntegerField(blank=True, null=True)),
                ('size', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('amazing_offer', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category_clothing', models.ManyToManyField(to='product.category_clothing')),
                ('category_color', models.ManyToManyField(to='product.category_color')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Dijitalgoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content1', models.CharField(max_length=255)),
                ('content2', models.CharField(blank=True, max_length=100, null=True)),
                ('content3', models.CharField(blank=True, max_length=255, null=True)),
                ('content4', models.CharField(blank=True, max_length=255, null=True)),
                ('content5', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.ImageField(upload_to='dititalgoods')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='dititalgoods')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='dititalgoods')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='dititalgoods')),
                ('more_details', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('off', models.IntegerField(blank=True, null=True)),
                ('warranty', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=False)),
                ('amazing_offer', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category_Dijitalgoods', models.ManyToManyField(to='product.category_dijitalgoods')),
                ('category_brand', models.ManyToManyField(to='product.category_brand')),
                ('category_color', models.ManyToManyField(to='product.category_color')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Homeappliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content1', models.CharField(max_length=255)),
                ('content2', models.CharField(blank=True, max_length=100, null=True)),
                ('content3', models.CharField(blank=True, max_length=255, null=True)),
                ('content4', models.CharField(blank=True, max_length=255, null=True)),
                ('content5', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.ImageField(upload_to='homeappliances')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='homeappliances')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='homeappliances')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='homeappliances')),
                ('more_details', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('off', models.IntegerField(blank=True, null=True)),
                ('warranty', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=False)),
                ('amazing_offer', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category_Homeappliances', models.ManyToManyField(to='product.category_homeappliances')),
                ('category_brand', models.ManyToManyField(to='product.category_brand')),
                ('category_color', models.ManyToManyField(to='product.category_color')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='Supermarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content1', models.CharField(max_length=255)),
                ('content2', models.CharField(blank=True, max_length=100, null=True)),
                ('content3', models.CharField(blank=True, max_length=255, null=True)),
                ('content4', models.CharField(blank=True, max_length=255, null=True)),
                ('content5', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.ImageField(upload_to='supermarkets')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='supermarkets')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='supermarkets')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='supermarkets')),
                ('more_details', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('off', models.IntegerField(blank=True, null=True)),
                ('exception_date', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('amazing_offer', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category_Supermarket', models.ManyToManyField(to='product.category_supermarket')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
