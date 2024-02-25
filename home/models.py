from contextlib import nullcontext
from django.db import models

# Create your models here.

class user(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True , blank=True)
    address =models.TextField(null=True , blank=True)
    def __str__(self):
        return self.name
    
class signup(models.Model):
    #id = models.AutoField()
    username = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(null=True , blank=True)
    def __str__(self):
        return self.username
    
class cow(models.Model):
    name = models.CharField(max_length=20,null=True)
    age = models.IntegerField()
    weight = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    per_kg_cost = models.IntegerField()
    description = models.CharField(max_length=200, default='Default Description')
    pic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default="")

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ->'+ ' ' + self.name + ' - ' + self.email
    
class protfolio(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default="")
    text = models.TextField()

    def __str__(self):
        return self.name
    
class cart(models.Model):
    cart_no = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255,default=True)
    phone = models.CharField(max_length=11)
    product_id = models.IntegerField(default=1)

    def __str__(self):
        return 'Message from ->'+ ' ' + self.product_name + ' - ' + self.phone

