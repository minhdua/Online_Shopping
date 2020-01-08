from rest_framework import serializers
from .models import Product
from apps.categories_and_labels.models import Category
from apps.shops.models import Shop
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        ModelClass = self.Meta.model
        shop = Shop.objects.get(pk=validated_data.pop('pk'))
        validated_data['shop']=shop
        print('shop',shop)
        try:
            instance = ModelClass._default_manager.create(**validated_data)
        except TypeError:
            msg = ("Error serializer products")
            raise TypeError(msg)
        return instance
