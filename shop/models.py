from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    image1 = models.ImageField(null=True, blank=True, upload_to="images/")
    image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    quantity = models.IntegerField()


class Deal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
