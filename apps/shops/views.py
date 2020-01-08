from apps.authentication.permissions import IsUserNormalOrReadOnly,IsAdmin
from apps.authentication.models import User
from rest_framework import generics
from .models import Shop
from .serializers import ShopSerializer
from .permissions import IsOwnerShopOrReadOnly
import django_filters.rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class ShopSpendingList(generics.ListAPIView):
    queryset = Shop.objects.filter(status=None)
    serializer_class = ShopSerializer
    permission_classes = (IsUserNormalOrReadOnly,)
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['name', 'id']

class ShopListCreate(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsUserNormalOrReadOnly,)
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['name', 'id','status']
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShopRU(generics.RetrieveUpdateAPIView):
    """
        function: Retrieve, update specific Shop
        permisson: User Normal -> retrive and update, other -> read only
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsOwnerShopOrReadOnly,)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class ShopStatus(generics.RetrieveUpdateAPIView):
    """
        function: Change status specific Shop
                None -> spending
                True -> actived
                False -> rejected
        permisson: Admin Only
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAdmin,)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
