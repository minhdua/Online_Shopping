from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *



class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['pk','email', 'username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )


        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )


        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        token = user.token
        DashBoard(token=token).save()
        return {
            'email': user.email,
            'token': token
        }

class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255, read_only=True)

class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('pk','email', 'username', 'password','is_active','is_superuser')
        read_only_fields = ('email',)


    def update(self, instance, validated_data):
        """Performs an update on a User."""
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance

class UserBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk','email', 'username','is_active')
        read_only_fields = ('email','username')

    def update(self, instance, validated_data):
        instance.block()
        return instance

class UserUnBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk','email', 'username','is_active')
        read_only_fields = ('email','username')

    def update(self, instance, validated_data):
        instance.unblock()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        read_only_fields = ('status',)

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)

class ShopActiveSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=128,
    min_length=8,write_only=True)
    token = ""
    def update(self, instance, validated_data):
        instance.active()
        token = instance.token
        DashBoard(token=token).save()
        return instance

    class Meta:
        model = Shop
        fields = ('name','address','phone','token')
        #read_only_fields = ('name','address','phone','token')

class ShopRejectSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=128,
    min_length=8,write_only=True,default="wrong informations")

    def update(self, instance, validated_data):
        if validated_data.get('content'):
            content = validated_data.get('content')
            #print(content)
        Message(content=content,shop=instance).save()
        instance.reject()#status = 'rejected'
        return instance
    class Meta:
        model = Shop
        fields = ('id','name','content')
        #read_only_fields = ('__all__',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)

class CartCreateSerializer(serializers.Serializer):

    def update(self, instance,pk, validated_data):
        product = instance
        user = request.user
        if validated_data.get('number'):
            number = validated_data.get('number')
            print(number)
        else: number = 1
        Cart(user=user,product=product,number=number).save()
        return {
            "detail":"added s:"
        }


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
