from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60,unique=True)
    describe = models.TextField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.name

class Label(models.Model):
    id = models.AutoField(primary_key=True)
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=60,unique=True)
    describe = models.TextField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.name
