from django.db import models

# Create your models here.

class Category_clothing(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Category_Dijitalgoods(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category_Homeappliances(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category_Beauty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category_Appliances(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Category_Supermarket(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Category_Child_and_baby(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name





class Product(models.Model):
    image = models.ImageField(upload_to='products')
    image1 = models.ImageField(upload_to='products', null=True ,blank=True)
    image2 = models.ImageField(upload_to='products',null=True,blank=True)
    image3 = models.ImageField(upload_to='products',null=True,blank=True)
    title = models.CharField(max_length=100)
    content= models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    off = models.IntegerField(default=0)
    warranty = models.CharField(max_length=255,null=True,blank=True)
    color = models.CharField(max_length=255,null=True,blank=True)

    category_clothing = models.ManyToManyField(Category_clothing,null=True,blank=True)
    category_Dijitalgoods = models.ManyToManyField(Category_Dijitalgoods,null=True,blank=True)
    category_Homeappliances = models.ManyToManyField(Category_Homeappliances,null=True,blank=True)
    category_Beauty = models.ManyToManyField(Category_Beauty,null=True,blank=True)
    category_Appliances = models.ManyToManyField(Category_Appliances,null=True,blank=True)
    category_Appliances = models.ManyToManyField(Category_Supermarket,null=True,blank=True)
    category_Child_and_baby = models.ManyToManyField(Category_Child_and_baby,null=True,blank=True)

    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'

    

 

