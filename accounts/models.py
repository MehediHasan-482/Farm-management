from django.db import models

# Create your models here.

class worker(models.Model):
    #w_id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True , blank=True)
    address =models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default="")

    
    def __str__(self):
        return self.name
    
class officer(models.Model):
    #o_id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True , blank=True)
    address =models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default="")

    
    def __str__(self):
        return self.name


