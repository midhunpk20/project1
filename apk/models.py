from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField(blank=True, null=True)  
    category = models.CharField(max_length=50)  
    stock_quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/')