# Generated by Django 5.0.6 on 2024-06-03 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('image1', models.ImageField(upload_to='products')),
                ('image2', models.ImageField(upload_to='products')),
                ('image3', models.ImageField(upload_to='products')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=255)),
                ('content2', models.CharField(max_length=100)),
                ('content3', models.CharField(max_length=255)),
                ('content4', models.CharField(max_length=255)),
                ('content5', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('warranty', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='product.category')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
