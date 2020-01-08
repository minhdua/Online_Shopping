from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','email','is_active','is_superuser','password']

    def create(self,validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.pop('password_confirm')
        print(password,password_confirm)
        if password != password_confirm :
            raise serializers.ValidationError(
                'confirm password not match!'
            )
        instance = User.objects.create_user(**validated_data)
        return instance

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_active','is_superuser','password']
        read_only_fields = ['username','email']
    def update(self, instance, validated_data):
        print(validated_data,)
        is_active = validated_data.pop("is_active",instance.is_active)
        is_superuser = validated_data.pop("is_superuser",instance.is_superuser)
        password = validated_data.pop('password',None)
        user = validated_data.pop('user')
        if user.is_superuser == True:
            instance.is_active = is_active
            instance.is_superuser = is_superuser
            instance.save()
            return instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
