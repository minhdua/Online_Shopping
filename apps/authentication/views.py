from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView,ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,UpdateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .renderers import UserJSONRenderer
from .serializers import (
    LogoutSerializer,LoginSerializer, RegistrationSerializer, UserSerializer,RegistrationSerializer,UserBlockSerializer, UserUnBlockSerializer,)
from rest_framework import generics
from .models import User,DashBoard
from .permissions import *
from django.views.decorators.csrf import csrf_exempt
import json

class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLoginAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.user
        request.session['user']=user
        return Response({"detail":"login successful"}, status=status.HTTP_200_OK)

class UserGetTokenAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserLogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LogoutSerializer
    def delete(self, request):
        print(request.session['user'])
        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META['HTTP_AUTHORIZATION'].split()[1]
            user = request.META['HTTP_AUTHORIZATION'].split()[0]
            print(user)
            try:
                dashboard = DashBoard.objects.get(token=token)
            except DashBoard.DoesNotExist:
                dashboard = DashBoard(token=token)
            dashboard.stop
            return Response({"message": "logout successful!"},status=status.HTTP_200_OK)

class UserListAPIView(ListAPIView):
    permission_classes = (IsAdmin,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserBlookAPIView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdmin,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserBlockSerializer

class UserUnBlookAPIView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdmin,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserUnBlockSerializer

class UserAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

from .models import *
from .serializers import *
# Create your views here.
from apps.authentication.permissions import IsAdmin

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdmin,)

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdmin,)

class LabelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (IsAdmin,)

class LabelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = (IsAdmin,)


class ShopListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShopRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsOwner,IsActiveShop,)

class ShopActiveAPIView(generics.UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopActiveSerializer
    permission_classes = (IsAdmin,)

class ShopRejectAPIView(generics.UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopRejectSerializer
    permission_classes = (IsAdmin,)

class ShopSpendingListAPIView(generics.ListAPIView):
    queryset = Shop.spending_objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAdmin,)

class ShopActiveListAPIView(generics.ListAPIView):
    queryset = Shop.active_objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAdmin,)

class ShopRejectListAPIView(generics.ListAPIView):
    queryset = Shop.reject_objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAdmin,)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsOwerShop,)
    def perform_create(self, serializer):
        serializer.save(shop=self.request.user)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsOwerShop,)

class CartCreateProductAPIView(APIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
    def post(self,request,pk):
        user = request.user
        product = Product.objects.get(pk=pk)
        try :
            number = request.data.get('number')
        except:
            number = 1
        try:
            cart = Cart.objects.get(product=product,user=user)
            cart.number = cart.number+number
            cart.save(update_fields=['number'])
        except Cart.DoesNotExist:
            Cart(user=user,product=product,number=number).save()
        return Response({'detail':'added successful'}, status=status.HTTP_201_CREATED)

class CartRemoveProductAPIView(APIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
    def delete(self,request,pk):
        user = request.user

        try:
            product = Product.objects.get(pk=pk)
            number = request.data.get('number')
        except Product.DoesNotExist:
            return Response({'detail':'product not found'}, status=status.HTTP_204_NO_CONTENT)
        else:
            number = product.number
        try:
            cart = Cart.objects.get(product=product,user=user)
            cart.number = cart.number-number
            print(cart.number)
            if cart.number <= 0:
                cart.delete()
            else :
                cart.save(update_fields=['number'])
        except Cart.DoesNotExist:
            return Response({'detail':'product not found in your cart'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail':'removed successful'}, status=status.HTTP_201_CREATED)

class CartDeleteAPIView(APIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
    def delete(self,request):
        user = request.user
        print(user)
        cart = Cart.objects.filter(user=user)
        if cart:
            cart.delete()
        else:
            return Response({'detail':'You have not added any products to your shopping cart'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail':'removed successful'}, status=status.HTTP_201_CREATED)

from django.core import serializers

class CartListAPIView(APIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user = request.user
        print(user)
        cart = json.loads(serializers.serialize('json', Cart.objects.all()))
        return Response(data=cart, status=status.HTTP_201_CREATED)


class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)
    #permission_classes = (IsOwner,IsActiveShop,)

class BillListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    """
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(shops=self.request.user)
    """

class BillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (IsAuthenticated,)
    #permission_classes = (IsOwner,IsActiveShop,)
