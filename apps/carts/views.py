from apps.authentication.permissions import IsUserNormalOrReadOnly,IsAdmin
from apps.authentication.models import User
from rest_framework import generics
from apps.shops.models import Shop
from .models import CartDetail
from .serializers import CartSerializer
import django_filters.rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class CartListCreate(generics.ListCreateAPIView):
    queryset = CartDetail.objects.all()
    serializer_class = CartSerializer
    #permission_classes = (IsUserNormalOrReadOnly,)
    def perform_create(self, serializer):

        serializer.save(user=self.request.user)
