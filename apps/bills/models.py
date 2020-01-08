from django.db import models

# Create your models here.
class Bill(models.Model):
    CHOICES = (
    (None,"Speding"),
    (True,"Confirmed"),
    (False,"cancelled")
    )
    id = models.AutoField(primary_key=True)
    status = models.NullBooleanField(max_length=60,choices=CHOICES,default=None)
    payment = models.CharField(max_length=60,default="cash")
    VAT = models.FloatField(default=1.5)
    ship = models.DecimalField(decimal_places=3, max_digits=60)
    total = models.DecimalField(decimal_places=3, max_digits=60)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
