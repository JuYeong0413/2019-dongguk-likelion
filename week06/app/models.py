from django.db import models

# Create your models here.
class Product(models.Model):
    objects = models.Manager()
    
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = "images/", null = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)