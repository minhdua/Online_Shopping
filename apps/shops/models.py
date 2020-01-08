from django.db import models
from apps.authentication.models import User
from apps.categories_and_labels.models import Category
# Create your models here.

class Shop(models.Model):
    CHOICES = (
    (True, "actived"),
    (False, "rejected"),
    (None, "spending"))
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60,unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    status = models.NullBooleanField(max_length=60,choices=CHOICES,default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="shop_user")
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
