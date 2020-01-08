from rest_framework import serializers
from .models import Shop
from apps.categories_and_labels.models import Category
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        ModelClass = self.Meta.model
        categories = validated_data.pop('categories')
        try:
            instance = ModelClass._default_manager.create(**validated_data)
        except TypeError:
            msg = ("Error")
            raise TypeError(msg)
        for cate in categories:
            category = Category.objects.get(pk=cate.id)
            instance.categories.add(category)
        return instance

    def update(self, instance, validated_data):
        categories = validated_data.pop('categories',None)
        user = validated_data.pop('user')
        if not user.is_superuser:
            validated_data['status'] = None
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if categories:
            cate_odd = instance.categories.all()
            for cate in cate_odd:
                instance.categories.remove(cate)
            for cate in categories:
                instance.categories.add(cate)
        return instance
