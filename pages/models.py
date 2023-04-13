from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete




# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField()


    # signal for customer add up

    @receiver(post_save, sender=User)
    def Createprofile(sender,instance,created, **kwargs):
        if created:
            user = instance
            profile = Customer.objects.create(
                user=user,
                name=user.first_name,
                email=user.email
            )
    

    def __str__(self):
        return self.name


   

class Product(models.Model):
    products = (
        ('Beauty_Health','Beauty_Health'),
        ('Confectioneries','Confectioneries'),
        ('Drinks','Drinks'),
        ('Grain_Flour','Grain_Flour'),
        ('Meat_vegetable','Meat_vegetable'),
        ('Species_oil','Species_oil'),
        ('Tuber','Tuber'),
        ('Untensiles','Untensiles'),
    )
    product_item = models.CharField(max_length=100, choices=products,default='Beauty_Health')
    name = models.CharField(max_length=100,blank=True)
    price = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    brief = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    postingDate = models.DateTimeField(default=datetime.now, blank=True)


    # signal for delete
    @receiver(post_delete, sender=Customer)
    def DeleteUser(sender,instance, **kwargs):
        user = instance.user
        user.delete()

    def __str__(self):
        return self.name

    


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE )
    cart_id = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    # created = models.DateTimeField(auto_now_add=True, blank=True)
    completed = models.BooleanField(default=False)
    # session_id = models.CharField(max_length=100,blank=True)

    @property
    def get_cart_total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.get_total for item in cartitems])
        return total
    
    @property
    def get_itemtotal(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    def __str__(self):
        return str(self.id)


class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


    @property
    def get_total(self):
        total = self.quantity * self.product.price
        if total == 0.00:
            self.delete()
        return total

    

    def __str__(self):
        return self.product.name
        

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.address