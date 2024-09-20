from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    date_created = models.DateTimeField()
    real_estate = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    STATUS_CHOICES = [
        ('F', 'Fixed price'),
        ('S', 'Accepts suggestions for price'),
        ('N', 'The price is not fixed')
    ]

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    date_and_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='advertisements/')
    price = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    new = models.BooleanField(default=True)

    def __str__(self):
        return self.name

