from django.db import models
from apps.products.models import Product
from apps.authentication.models import User
from apps.bills.models import Bill

class CartDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quality = models.IntegerField(default=1)
    add_date = models.DateTimeField(auto_now=True)
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE,default=None)
