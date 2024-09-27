from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator
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




# پوشاک
class Clothing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brief_description = models.TextField(null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    category_clothing = models.ManyToManyField(Category_clothing)

    image1 = models.ImageField(upload_to='clothings')
    image2 = models.ImageField(upload_to='clothings', null=True ,blank=True)
    image3 = models.ImageField(upload_to='clothings',null=True,blank=True)
    image4 = models.ImageField(upload_to='clothings',null=True,blank=True)


   
    
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    stock = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=255)

    status = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'

    def get_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)
    
    def is_discounted(self):
        return self.discount_percent != 0
 

# کالای دیجیتال 
class Dijitalgoods(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brief_description = models.TextField(null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    category_Dijitalgoods = models.ManyToManyField(Category_Dijitalgoods)

    image1 = models.ImageField(upload_to='dititalgoods')
    image2 = models.ImageField(upload_to='dititalgoods', null=True ,blank=True)
    image3 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    image4 = models.ImageField(upload_to='dititalgoods',null=True,blank=True)
    
    
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    stock = models.PositiveIntegerField(default=0)
    warranty = models.CharField(max_length=255,null=True,blank=True)

    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'

    def get_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)
    
    def is_discounted(self):
        return self.discount_percent != 0


# لوازم خانگی
class Homeappliances(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brief_description = models.TextField(null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    category_Homeappliances = models.ManyToManyField(Category_Homeappliances)


    image1 = models.ImageField(upload_to='homeappliances')
    image2 = models.ImageField(upload_to='homeappliances', null=True ,blank=True)
    image3 = models.ImageField(upload_to='homeappliances',null=True,blank=True)
    image4 = models.ImageField(upload_to='homeappliances',null=True,blank=True)
    
    

    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    stock = models.PositiveIntegerField(default=0)
    warranty = models.CharField(max_length=255,null=True,blank=True)
   
    

    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'

    def get_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)
    
    def is_discounted(self):
        return self.discount_percent != 0



# زیبایی  
class Beauty(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brief_description = models.TextField(null=True,blank=True)
    category_Beauty = models.ManyToManyField(Category_Beauty)
    slug = models.SlugField(allow_unicode=True,unique=True)

    image1 = models.ImageField(upload_to='beauty')
    image2 = models.ImageField(upload_to='beauty', null=True ,blank=True)
    image3 = models.ImageField(upload_to='beauty',null=True,blank=True)
    image4 = models.ImageField(upload_to='beauty',null=True,blank=True)
    
    

    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    stock = models.PositiveIntegerField(default=0)
    exception_date = models.CharField(max_length=255)
   

    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'

    def get_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)
    
    def is_discounted(self):
        return self.discount_percent != 0


# لوازم برقی
class Appliances(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brief_description = models.TextField(null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    category_Appliances = models.ManyToManyField(Category_Appliances)

    image1 = models.ImageField(upload_to='appliances')
    image2 = models.ImageField(upload_to='appliances', null=True ,blank=True)
    image3 = models.ImageField(upload_to='appliances',null=True,blank=True)
    image4 = models.ImageField(upload_to='appliances',null=True,blank=True)
    
    
    
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    stock = models.PositiveIntegerField(default=0)
    warranty = models.CharField(max_length=255)
   


    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'

    def get_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)
    
    def is_discounted(self):
        return self.discount_percent != 0
    


# سوپر مارکت 
class Supermarket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brief_description = models.TextField(null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    category_Supermarket = models.ManyToManyField(Category_Supermarket)


    image1 = models.ImageField(upload_to='supermarkets')
    image2 = models.ImageField(upload_to='supermarkets', null=True ,blank=True)
    image3 = models.ImageField(upload_to='supermarkets',null=True,blank=True)
    image4 = models.ImageField(upload_to='supermarkets',null=True,blank=True)
    
   
    
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    stock = models.PositiveIntegerField(default=0)
    exception_date = models.CharField(max_length=255)
   

    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'


    def get_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)
    
    def is_discounted(self):
        return self.discount_percent != 0


#  کودک و نوزاد 
class Child_and_baby(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brief_description = models.TextField(null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    category_Child_and_baby = models.ManyToManyField(Category_Child_and_baby)

    image1 = models.ImageField(upload_to='child_and_baby')
    image2 = models.ImageField(upload_to='child_and_baby', null=True ,blank=True)
    image3 = models.ImageField(upload_to='child_and_baby',null=True,blank=True)
    image4 = models.ImageField(upload_to='child_and_baby',null=True,blank=True)
    
    
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_percent = models.IntegerField(default=0,validators = [MinValueValidator(0),MaxValueValidator(100)])
    stock = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=255)
    
  

    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    
   
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.title[:30] + '...'

    def get_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)
    
    def is_discounted(self):
        return self.discount_percent != 0