from django.db import models
from django.contrib.auth.models import User
from customer . models import Customer

# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    
    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField(upload_to = "product/images/")
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    category = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    stock = models.IntegerField()
    
    def __str__(self):
        return f"Product Name: {self.title} &  Price: ${self.price}"



STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    email = models.EmailField(max_length = 100, blank = True, null = True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"Customer Name: {self.reviewer.user.first_name} {self.reviewer.user.last_name} ; Buying Product Name: {self.product.title}"