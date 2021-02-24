from django.db import models

# Create your models here.

CATEGORY=(('甘口','甘口'),('辛口','辛口'),("旨口","旨口"))

class Product(models.Model):
    product=models.CharField(max_length=100)
    Description=models.TextField()
    postdate=models.DateField(auto_now_add=True)
    category=models.CharField(
        max_length=50,
        choices=CATEGORY
    )
    views=models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.product