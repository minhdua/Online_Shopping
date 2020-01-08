from rest_framework import permissions

class IsOwnerShopOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in ['PUT','PATCH']:
            return obj.user == user
        else : return True
