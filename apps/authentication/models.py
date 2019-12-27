import jwt
from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def block(self):
        self.is_active = False
        self.save(update_fields=['is_active'])

    def unblock(self):
        self.is_active = True
        self.save(update_fields=['is_active'])

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.username

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class DashBoard(models.Model):
    token = models.CharField(max_length=255,db_index=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.token
    @property
    def stop(self):
        self.is_active = False
        self.save()

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.name

class Label(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,unique=True)
    describe = models.TextField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.name

"""
    informations of shops
"""
class ShopSpendingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="spending")
class ShopActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="actived")
class ShopRejectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="rejected")

class Shop(models.Model):
    s = ((0,'waiting'),(1,'actived'),(-1,'rejected'))
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    status = models.CharField(max_length=30,choices=s,default='spending')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    objects = models.Manager()
    spending_objects = ShopSpendingManager()
    active_objects = ShopActiveManager()
    reject_objects = ShopRejectManager()
    def __str__(self):
        return self.name

    @property
    def token(self):
        return self._generate_jwt_token()
    #@property
    def active(self):
        self.status = "actived"
        self.save(update_fields=['status'])

    #@property
    def reject(self):
        self.status = "rejected"
        self.save(update_fields=['status'])

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')



class Message(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)
    number = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=3,max_digits=100)
    image = models.CharField(max_length=30,default="a/b/c")
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,null=True)
    label = models.ForeignKey(Label,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(default=1)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name




class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)
    VAT = models.FloatField(default=1.5)
    ship = models.DecimalField(decimal_places=3, max_digits=100)
    def __str__(self):
        return self.name
