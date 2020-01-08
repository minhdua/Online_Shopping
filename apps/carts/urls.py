from django.urls import path,include
from .views import *

appname = 'carts'
urlpatterns = [
    path('',CartListCreate.as_view()),
]
