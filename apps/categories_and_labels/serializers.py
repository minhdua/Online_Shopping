from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        ordering_fields = ('id',)
        ordering = ['-id']

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"
    def create(self, validated_data):
        ModelClass = self.Meta.model
        name = validated_data.get('name')
        categories = validated_data.pop('categories')
        print(validated_data)
        print(categories)
        print(name)
        try:
            instance = ModelClass._default_manager.create(name=name)
            print('instance',instance)
        except TypeError:
            msg = ("Error")
            raise TypeError(msg)
        print(type(categories))
        for category in categories:
            instance.categories.add(category)
        return instance
