from rest_framework import permissions
from .models import *

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            pk=request.session['user']
            user = User.objects.get(pk=pk)
        except:
            return False
        return user.is_superuser

class IsLogin(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user = request.session['user']
            return True
        except:
            return False

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            user = User.objects.get(pk = request.session['user'] )
            print(obj.pk == user.pk or user.is_superuser)
            return (obj.pk == user.pk or user.is_superuser )
        except:
            return False



class IsOwnerShopOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            user = User.objects.get(pk = request.session['user'] )
            print(obj.user == user or user.is_superuser)
            return (obj.user == user or user.is_superuser )
        except:
            return False

class IsActiveShop(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.status == 'actived'

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_admin
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_admin
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_admin
        elif view.action == 'destroy':
            return request.user.is_admin
        else:
            return False
