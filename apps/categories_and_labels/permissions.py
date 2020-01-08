from rest_framework import permissions
from .models import *

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_superuser
