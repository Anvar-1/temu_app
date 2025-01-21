from django.contrib.auth.models import AbstractUser
from django.db import models
from ..products.models import Product

class User(AbstractUser):
    phone = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email']


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s cart: {self.product.title} (x{self.quantity})"