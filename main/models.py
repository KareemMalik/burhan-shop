import uuid
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('football shoes', 'Football Shoes'),
        ('training gear', 'Training Gear'),
        ('training jacket', 'Training Jacket'),
        ('accessories', 'Accessories'),
        ('equipments', 'Equipments'),
    ]

    name = models.CharField(max_length=255, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=5, null=True, blank=True)
    product_views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.product_views +=1
        self.save()
    
