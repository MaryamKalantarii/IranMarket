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

class Category_brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Brandimage')

    def __str__(self):
        return self.name


class Clothing(models.Model):
    title = models.CharField(max_length=255)
    content1 = models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)

    image1 = models.ImageField(upload_to='clothings')
    image2 = models.ImageField(upload_to='clothings', null=True ,blank=True)
    image3 = models.ImageField(upload_to='clothings',null=True,blank=True)
    image4 = models.ImageField(upload_to='clothings',null=True,blank=True)

    more_details = models.CharField(max_length=255)
    category_clothing = models.ManyToManyField(Category_clothing)
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    off = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=255)

    status = models.BooleanField(default=False)
    amazing_offer = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'


 


class Dijitalgoods(models.Model):
    title = models.CharField(max_length=100)
    content1= models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)

    image1 = models.ImageField(upload_to='dititalgoods')
    image2 = models.ImageField(upload_to='dititalgoods', null=True ,blank=True)
    image3 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    image4 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Dijitalgoods = models.ManyToManyField(Category_Dijitalgoods)
    category_brand = models.ManyToManyField(Category_brand)

    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    off = models.IntegerField(null=True, blank=True)
    warranty = models.CharField(max_length=255,null=True,blank=True)

    status = models.BooleanField(default=False)
    amazing_offer = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'



class Homeappliances(models.Model):
    title = models.CharField(max_length=100)
    content1= models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)

    image1 = models.ImageField(upload_to='dititalgoods')
    image2 = models.ImageField(upload_to='dititalgoods', null=True ,blank=True)
    image3 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    image4 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Dijitalgoods = models.ManyToManyField(Category_Dijitalgoods)
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    off = models.IntegerField(null=True, blank=True)
    warranty = models.CharField(max_length=255,null=True,blank=True)
   

    
    category_Homeappliances = models.ManyToManyField(Category_Homeappliances)
    

    status = models.BooleanField(default=False)
    amazing_offer = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'


class Beauty(models.Model):
    title = models.CharField(max_length=100)
    content1= models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)

    image1 = models.ImageField(upload_to='dititalgoods')
    image2 = models.ImageField(upload_to='dititalgoods', null=True ,blank=True)
    image3 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    image4 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Beauty = models.ManyToManyField(Category_Beauty)
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    off = models.IntegerField(null=True, blank=True)
    exception_date = models.CharField(max_length=255)
   

    

    status = models.BooleanField(default=False)
    amazing_offer = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'



class Appliances(models.Model):
    title = models.CharField(max_length=100)
    content1= models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)

    image1 = models.ImageField(upload_to='dititalgoods')
    image2 = models.ImageField(upload_to='dititalgoods', null=True ,blank=True)
    image3 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    image4 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Appliances = models.ManyToManyField(Category_Appliances)
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    off = models.IntegerField(null=True, blank=True)
    warranty = models.CharField(max_length=255)
   


    status = models.BooleanField(default=False)
    amazing_offer = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'


class Supermarket(models.Model):
    title = models.CharField(max_length=100)
    content1= models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)

    image1 = models.ImageField(upload_to='dititalgoods')
    image2 = models.ImageField(upload_to='dititalgoods', null=True ,blank=True)
    image3 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    image4 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Supermarket = models.ManyToManyField(Category_Supermarket)
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    off = models.IntegerField(null=True, blank=True)
    exception_date = models.CharField(max_length=255)
   

    

    status = models.BooleanField(default=False)
    amazing_offer = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'


class Child_and_baby(models.Model):
    title = models.CharField(max_length=100)
    content1= models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)

    image1 = models.ImageField(upload_to='dititalgoods')
    image2 = models.ImageField(upload_to='dititalgoods', null=True ,blank=True)
    image3 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    image4 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Child_and_baby = models.ManyToManyField(Category_Child_and_baby)
    category_brand = models.ManyToManyField(Category_brand)
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    off = models.IntegerField(null=True, blank=True)
    exception_date = models.CharField(max_length=255)
   

    status = models.BooleanField(default=False)
    amazing_offer = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'
