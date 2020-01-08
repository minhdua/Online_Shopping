from django.urls import path
from .views import ProductList,ProductCreate,ProductR,ProductRUD

appname = 'products'
urlpatterns = [
    path('',ProductCreate.as_view()),
    path('list/',ProductList.as_view()),
    path('<int:pk>/',ProductRUD.as_view()),
    path('<int:pk>/detail/',ProductR.as_view()),
]
