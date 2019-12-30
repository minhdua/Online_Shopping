from django.urls import path

from .views import *
from . import tests


app_name = 'authentication'
urlpatterns = [
    path('registers/', UserRegistrationAPIView.as_view()),
    path('token/', UserGetTokenAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('test/', TestAPIView.as_view()),
    path('list/', UserListAPIView.as_view()),
    path('<int:pk>/detail/',UserAPIView.as_view()),

    path('<int:pk>/block/',UserBlookAPIView.as_view()),
    path('<int:pk>/unblock/',UserUnBlookAPIView.as_view()),
    path('logout/',UserLogoutAPIView.as_view()),

    path('category/',CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/',CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('label/',LabelListCreateAPIView.as_view()),
    path('label/<int:pk>/',LabelRetrieveUpdateDestroyAPIView.as_view()),

    path('shops/',ShopListCreateAPIView.as_view()),
    path('shops/<int:pk>/',ShopRetrieveUpdateAPIView.as_view()),
    path('shops/<int:pk>/accept/',ShopActiveAPIView.as_view()),
    path('shops/<int:pk>/reject/',ShopRejectAPIView.as_view()),
    path('shops/spending/',ShopSpendingListAPIView.as_view()),
    path('shops/activated/',ShopActiveListAPIView.as_view()),
    path('shops/rejected/',ShopRejectListAPIView.as_view()),
    path('shops/<int:pk>/token/',ShopGetTokenAPIView.as_view()),
    path('shops/login/',ShopLoginAPIView.as_view()),

    path('products/',ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/',ProductRetrieveUpdateDestroyAPIView.as_view()),


    path('products/',ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/',ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('products/<int:pk>/addcart/',ProductAddCartAPIView.as_view()),
    path('products/<int:pk>/removecart/',ProductRemoveCartAPIView.as_view()),

    path('carts/',CartListAPIView.as_view()),
    #path('carts/',CartListCreateAPIView.as_view()),
    path('carts/<int:pk>/',CartRetrieveUpdateDestroyAPIView.as_view()),
    path('carts/delete/',CartDeleteAPIView.as_view()),
    path('bills/',BillListCreateAPIView.as_view()),
    path('bills/<int:pk>/',BillRetrieveUpdateDestroyAPIView.as_view()),
]
