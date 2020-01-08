from rest_framework import serializers
from .models import Bill

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
"""
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
"""
