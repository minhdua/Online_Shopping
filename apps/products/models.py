from django.db import models
from apps.shops.models import Shop
from apps.categories_and_labels.models import Label
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60,unique=True)
    amount = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=3,max_digits=60)
    image = models.CharField(max_length=255,default="a/b/c")
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,null=True)
    label = models.ForeignKey(Label,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
