from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to='products')
    image1 = models.ImageField(upload_to='products')
    image2 = models.ImageField(upload_to='products')
    image3 = models.ImageField(upload_to='products')
    title = models.CharField(max_length=255)
    content= models.CharField(max_length=255)
    content2= models.CharField(max_length=255)
    content3= models.CharField(max_length=255)
    content4= models.CharField(max_length=255)
    content5= models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    number = models.IntegerField()
    warranty = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'

    

 

