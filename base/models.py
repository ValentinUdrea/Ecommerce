from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Here we will create our database

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Whenever a user that created a product gets deleted, the product will be se to NULL -> so that the product is not deleted  
    name = models.CharField(max_length=200, null=True, blank=True) # We can fill out a form -> and not have this element completed
    image = models.ImageField(null=True, blank=True)
    brand =  models.CharField(max_length=200, null=True, blank=True)
    category =  models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True) # This means we can write a longer field
    rating = models.DecimalField(max_digits=7,decimal_places=2, null=True,blank=True )
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price =  models.DecimalField(max_digits=7,decimal_places=2 , null=True,blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True) # Created at will take a snapshot of when the product was first created
    _id = models.AutoField(primary_key=True, editable=False) # This is going to tell django to use this as the id instead of what it originally wanted -> editable = false, becouse we dont want anyone to edit this fieldm becouse if we do, it will conflict with out database and its going to cause issues

    def __str__(self):
        return self.name # Instead of ProductOject -> will change the name of the product in Django administration with the variable name
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)
    
class Order(models.Model):
     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
     paymentMethod =  models.CharField(max_length=200, null=True, blank=True)
     taxPrice = models.DecimalField(max_digits=7,decimal_places=2 , null=True,blank=True)
     shippingPrice = models.DecimalField(max_digits=7,decimal_places=2 , null=True,blank=True)
     totalPrice = models.DecimalField(max_digits=7,decimal_places=2 , null=True,blank=True)
     isPaid = models.BooleanField(default=False)
     paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
     isDelivered = models.BooleanField(default=False)
     deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
     createdAt = models.DateTimeField(auto_now_add=True)
     _id = models.AutoField(primary_key=True, editable=False)

     def __str__(self):
         return str(self.createdAt) # To see it on the admin panel, it must become a string. This function does that
     
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order =  models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7,decimal_places=2 , null=True,blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class ShippingAdress(models.Model):
     order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True,blank=True)
     address = models.CharField(max_length=200, null=True, blank=True)
     city =  models.CharField(max_length=200, null=True, blank=True)
     postalCode =  models.CharField(max_length=200, null=True, blank=True)
     country =  models.CharField(max_length=200, null=True, blank=True)
     shippingPrice = models.DecimalField(max_digits=7,decimal_places=2 , null=True,blank=True)
     _id = models.AutoField(primary_key=True, editable=False)
     def __str__(self):
         return str(self.address)


 

    

    