from django.db import models

class Menu_items(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    prize = models.DecimalField(max_digits=10, decimal_places=2) 
    offer = models.CharField(max_length=100,default=False)  
    image = models.ImageField(upload_to='uploads/')
    hide = models.CharField(max_length=100 ,default= False) 

class Order(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    prize = models.IntegerField()
    quantity = models.IntegerField()
    result = models.CharField(max_length=100, default="pending") 
    tablenumber = models.CharField(max_length=100)

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200) 

class Category(models.Model):
    Category_name = models.CharField(max_length=100)
    Category_image = models.ImageField(upload_to='uploads/')  
