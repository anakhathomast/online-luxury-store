from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class Customer_Reg(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True)
    con_password=models.CharField(max_length=50,null=True)

class Seller_Reg(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True)
    con_password=models.CharField(max_length=50,null=True)

class Categ(models.Model):
    name=models.CharField(max_length=200,unique=True)

class Product(models.Model):
    name=models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='media/', null=True)
    desc=models.TextField(null=True)
    stock=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    category=models.TextField(null=True)
    seller=models.ForeignKey(Seller_Reg,on_delete=models.CASCADE,null=True)
    catg=models.ForeignKey(Categ,on_delete=models.CASCADE,null=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0,null=True)
    total = models.CharField(max_length=100, null=True)

    payment = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    delivery = models.CharField(max_length=100,null=True)
    billstatus = models.CharField(max_length=100,null=True)
    seller = models.ForeignKey(Seller_Reg, on_delete=models.CASCADE, null=True)

class Checkout_details(models.Model):
    firstname=models.CharField(max_length=100,null=True)
    lastname=models.CharField(max_length=100,null=True)
    phonenumber=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=250,null=True)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    feedback = models.CharField(max_length=500, null=True)