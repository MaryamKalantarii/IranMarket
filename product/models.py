from django.db import models

# Create your models here.

class Category_clothing(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return self.name
    
class Category_Dijitalgoods(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)
    def __str__(self):
        return self.name

class Category_Homeappliances(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return self.name


class Category_Beauty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category_Appliances(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return self.name
    
class Category_Supermarket(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return self.name
    

class Category_Child_and_baby(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return self.name

class Category_brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Brandimage')
    slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return self.name


class Category_color(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='colors')
    slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return self.name







class Clothing(models.Model):
    title = models.CharField(max_length=255)
    content1 = models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)

    image1 = models.ImageField(upload_to='clothings')
    image2 = models.ImageField(upload_to='clothings', null=True ,blank=True)
    image3 = models.ImageField(upload_to='clothings',null=True,blank=True)
    image4 = models.ImageField(upload_to='clothings',null=True,blank=True)

    more_details = models.CharField(max_length=255)
    category_clothing = models.ManyToManyField(Category_clothing)
    category_color = models.ManyToManyField(Category_color)
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
    slug = models.SlugField(allow_unicode=True,unique=True)

    image1 = models.ImageField(upload_to='dititalgoods')
    image2 = models.ImageField(upload_to='dititalgoods', null=True ,blank=True)
    image3 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    image4 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Dijitalgoods = models.ManyToManyField(Category_Dijitalgoods)
    category_brand = models.ManyToManyField(Category_brand)
    category_color = models.ManyToManyField(Category_color)


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
    slug = models.SlugField(allow_unicode=True,unique=True)

    image1 = models.ImageField(upload_to='homeappliances')
    image2 = models.ImageField(upload_to='homeappliances', null=True ,blank=True)
    image3 = models.ImageField(upload_to='homeappliances',null=True,blank=True)
    image4 = models.ImageField(upload_to='homeappliances',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Homeappliances = models.ManyToManyField(Category_Homeappliances)
    category_color = models.ManyToManyField(Category_color)
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


class Beauty(models.Model):
    title = models.CharField(max_length=100)
    content1= models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)

    image1 = models.ImageField(upload_to='beauty')
    image2 = models.ImageField(upload_to='beauty', null=True ,blank=True)
    image3 = models.ImageField(upload_to='beauty',null=True,blank=True)
    image4 = models.ImageField(upload_to='beauty',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Beauty = models.ManyToManyField(Category_Beauty)
    category_color = models.ManyToManyField(Category_color)
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



class Appliances(models.Model):
    title = models.CharField(max_length=100)
    content1= models.CharField(max_length=255)
    content2= models.CharField(max_length=100, null=True,blank=True)
    content3= models.CharField(max_length=255,null=True,blank=True)
    content4= models.CharField(max_length=255,null=True,blank=True)
    content5= models.CharField(max_length=255,null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)

    image1 = models.ImageField(upload_to='appliances')
    image2 = models.ImageField(upload_to='appliances', null=True ,blank=True)
    image3 = models.ImageField(upload_to='appliances',null=True,blank=True)
    image4 = models.ImageField(upload_to='appliances',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Appliances = models.ManyToManyField(Category_Appliances)
    category_color = models.ManyToManyField(Category_color)
    category_brand = models.ManyToManyField(Category_brand)

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
    slug = models.SlugField(allow_unicode=True,unique=True)

    image1 = models.ImageField(upload_to='supermarkets')
    image2 = models.ImageField(upload_to='supermarkets', null=True ,blank=True)
    image3 = models.ImageField(upload_to='supermarkets',null=True,blank=True)
    image4 = models.ImageField(upload_to='supermarkets',null=True,blank=True)
    
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
    slug = models.SlugField(allow_unicode=True,unique=True)

    image1 = models.ImageField(upload_to='child_and_baby')
    image2 = models.ImageField(upload_to='child_and_baby', null=True ,blank=True)
    image3 = models.ImageField(upload_to='child_and_baby',null=True,blank=True)
    image4 = models.ImageField(upload_to='child_and_baby',null=True,blank=True)
    
    more_details = models.CharField(max_length=255)
    category_Child_and_baby = models.ManyToManyField(Category_Child_and_baby)
    category_color = models.ManyToManyField(Category_color)
    size = models.CharField(max_length=255)
    
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    off = models.IntegerField(null=True, blank=True)

   

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
