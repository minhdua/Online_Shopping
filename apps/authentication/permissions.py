from rest_framework import permissions
from .models import *

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
class AllowAnyCreateOrAdminList(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            print(request.user)
            return request.user.is_superuser
        else : return True
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
            user = request.user
            if request.method in ['GET','PUT']:
                print('obj.pk=',obj.pk,'user.pk=',user.pk,'user.is_superuser=',user.is_superuser)
                return obj.pk == user.pk or user.is_superuser
            return False

class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return true
    def has_object_permission(self, request, view, obj):
        try:
            user = User.objects.get(pk = request.session['user'] )
            shop = Shop.objects.get(pk = request.session['shop'] )
            if request.method == 'GET':
                return user.is_active
            elif request.method in ['POST','PUT','PATCH','DELETE']:
                return obj.shop == shop or user.is_superuser
        except:
            return False

class IsUserNormalOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        elif request.method == "POST":
            return (not request.user.is_superuser) and request.user.is_active
        else: return False

class IsOwnerShopOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(pk=request.session['user'])
        if request.method == 'GET':
            return user.is_active
        return False

    def has_object_permission(self, request, view, obj):
        print('hello')
        try:
            user = User.objects.get(pk = request.session['user'] )
            if request.method == 'GET':
                print(obj.user,' ',user)
                return obj.user == user or user.is_superuser
        except:
            return False

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(pk=request.session['user'])
        action = request.method
        print(type(action),action)
        print(user.is_staff)
        if action == 'GET':
            return user.is_active
        if action in ('PUT','DELETE','POST'):
            return user.is_superuser

class IsLogin(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user = request.session['user']
            return True
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
