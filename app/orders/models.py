from django.db import models
from app.users.models import User
from app.products.models import Product

class Order(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Naqd pul'),
        ('card', 'Karta'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),         # Kutilmoqda
        ('shipped', 'Shipped'),         # Jo'natilgan
        ('delivered', 'Delivered'),     # Yetkazilgan
        ('canceled', 'Canceled'),       # Bekor qilingan
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_expiry = models.CharField(max_length=5, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
