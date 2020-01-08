from rest_framework import serializers
from .models import CartDetail
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'
