from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(max_length=500)
    flip_thumbnail = models.BooleanField(default=False)
    category = models.CharField(max_length=255) 
    is_featured = models.BooleanField(default=False)
    size = models.CharField(max_length=50, blank=True, null=True)
    rating = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    total_sales = models.IntegerField(default=0)
    

    # anggapannya enum type
    class Brand(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255, unique=True)
        
        def __str__(self):
            return self.name

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    persona = models.TextField()
    
class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    stock = models.IntegerField()
    