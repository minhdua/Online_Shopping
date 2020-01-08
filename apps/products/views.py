from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics
from apps.authentication.permissions import IsUserNormalOrReadOnly,IsAdmin
from apps.authentication.models import User
from .models import Product
from .permissions import IsOwnerShopOrReadOnly
from .serializers import ProductSerializer
import django_filters.rest_framework as filters

# Create your views here.
class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsOwnerShopOrReadOnly,)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(pk=kwargs['shop_pk'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['name', 'id','label','shop']

class ProductRUD(generics.RetrieveUpdateDestroyAPIView):
    """
        function: Retrieve, update specific Product
        permisson: User owrner -> retrive and update, other -> read only
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsOwnerShopOrReadOnly,)

class ProductR(generics.RetrieveAPIView):
    """
        function: Retrieve, update specific Product
        permisson: User owrner -> retrive and update, other -> read only
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = (IsOwnerShopOrReadOnly,)
