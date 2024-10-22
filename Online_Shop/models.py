from django.db import models

class Person(models.Model):
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=False)
    email = models.EmailField(max_length=100)


class Register(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)





class Customer(models.Model):
    user = models.OneToOneField(Register, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)



class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)