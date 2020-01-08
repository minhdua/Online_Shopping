from rest_framework import permissions
from apps.shops.models import Shop
class IsOwnerShopOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print('shop ===== ',view.kwargs['shop_pk'])
        shop = Shop.objects.get(pk=view.kwargs['shop_pk'])
        user = request.user
        print('permission',user)
        if request.method == "GET":
            return True
        else: return shop.user == user
    def has_object_permission(self, request, view, obj):
        shop = Shop.objects.get(pk=view.kwargs['shop_pk'])
        if request.method == "GET":
            return True
        else: return obj.shop == shop
