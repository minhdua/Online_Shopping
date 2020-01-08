from django.urls import path,include
from .views import BillListCreate,BillRUD

appname = 'bills'
urlpatterns = [
    path('',BillListCreate.as_view()),
    path('<int:pk>/',BillRUD.as_view()),
]
