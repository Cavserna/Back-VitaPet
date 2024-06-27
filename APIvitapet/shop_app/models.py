from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorylist')
    
    
    def __str__(self):
        return str(self.name)
    

class Order(models.Model):
    user = models.ForeignKey('user_app.Account', on_delete=models.CASCADE, related_name='userlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productlist')
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    addres =models.CharField(max_length=100)
    
    
    def __str__(self):
        return str(self.user)