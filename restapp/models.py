from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    RATINGS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product_name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount_price = models.DecimalField(max_digits=20, decimal_places=2)
    product_image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    production_date = models.DateField(blank=True, null=True) 
    expiry_date = models.DateField()
    ratings = models.IntegerField(choices=RATINGS)

    def __str__(self):
        return self.name

