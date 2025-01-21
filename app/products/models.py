from django.db import models

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', related_name='subcategories_set', on_delete=models.CASCADE)  # o'zgartirdik

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    subcategory = models.ManyToManyField(Subcategory, blank=True, related_name='categories')  # o'zgartirdik

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='products/')
    datetime = models.DateTimeField()
    amount = models.PositiveIntegerField()
    dostavka = models.BooleanField(default=False)
    star = models.FloatField()
    comment = models.TextField(blank=True)
    like = models.PositiveIntegerField(default=0)
    aksiya = models.BooleanField(default=False)
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title