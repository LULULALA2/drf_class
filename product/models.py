import datetime
from datetime import timedelta

from django.db import models

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    thumbnail = models.ImageField(blank=True)
    desc = models.TextField(max_length=500)
    registration_date = models.DateField(auto_now_add=True)
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=(datetime.datetime.now()+timedelta(days=7)))
