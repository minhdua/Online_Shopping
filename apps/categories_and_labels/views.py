from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Category,Label
from .permissions import (IsAdminOrReadOnly,)
from .serializers import CategorySerializer,LabelSerializer
from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
import django_filters.rest_framework as filters
class CategoryListCreate(generics.ListCreateAPIView):
    """
        function: Retrieve all categories in the database
               or Create and add a category to the database
        permissions:Admin -> create and list
                    Other -> list
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['name', 'id']
#############################################################################
class CategoryRUD(generics.RetrieveUpdateDestroyAPIView):
    """
        function: Retrieve, update, delete specific Category
        permisson: admin -> governor, other -> read only
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)

#############################################################################
class LabelListCreate(generics.ListCreateAPIView):
    """
        function: Retrieve all labels in the database
                or Create label to the database
        permissions: Anyone
    """
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (IsAdminOrReadOnly,)
    #filter_backends = [filters.DjangoFilterBackend]
    #filterset_fields = ['name', 'id','categories']
#############################################################################
class LabelRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (IsAdminOrReadOnly,)
#############################################################################
