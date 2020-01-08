from django.urls import path,include
from .views import ShopListCreate,ShopRU,ShopStatus,ShopSpendingList

appname = 'shops'
urlpatterns = [
    path('',ShopListCreate.as_view()),
    path('spending/',ShopSpendingList.as_view()),
    path('<int:pk>/',ShopRU.as_view()),
    path('<int:pk>/status/',ShopStatus.as_view()),
    path('<int:shop_pk>/products/',include(('apps.products.urls','products'),namespace='products')),
]
