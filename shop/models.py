from django.db import models

class Product(models.Model):

    prod_id= models.AutoField
    prod_name= models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    subcategory =models.CharField(max_length=50, default="")
    price= models.IntegerField(default= 0)
    desc= models.CharField(max_length=300)
    image= models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.prod_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
  
