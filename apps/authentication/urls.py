from django.urls import path
from .views import UserListCreate,UserLogin,UserRU,UserLogout
from . import tests


app_name = 'authentication'
urlpatterns = [
    path('', UserListCreate.as_view()),
    path('login/', UserLogin.as_view()),
    path('<int:pk>/detail/',UserRU.as_view()),
    path('logout/',UserLogout.as_view()),
]
