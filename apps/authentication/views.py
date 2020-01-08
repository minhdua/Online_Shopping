from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .renderers import UserJSONRenderer
from .serializers import *
from .models import User
from .permissions import *
from django.contrib.auth.hashers import check_password
import django_filters.rest_framework as filters
#####################################################################
class UserListCreate(generics.ListCreateAPIView):
    """
        Register new User
        POST: email, username, password1, password2
    """
    queryset = User.objects.all()
    permission_classes = (AllowAnyCreateOrAdminList,IsAuthenticated)
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id','username','email','is_active','is_superuser']
    def perform_create(self, serializer):
        serializer.save(password_confirm=self.request.data.get('password_confirm'))

#####################################################################
class UserLogin(generics.CreateAPIView):
    """
        Login an account,
        return token if account exist in database
        else raise account not exist

        POST: email,password
    """
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get("username",None)
        email = request.data.get("email",None)
        password = request.data.get("password",None)
        if username is None:
            if email is None:
                return Response({"error":"input username or email"}, status=status.HTTP_204_NO_CONTENT)
            else:
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    return Response({"error":"email not exist"}, status=status.HTTP_204_NO_CONTENT)
        else:
            try :
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({"error":"username not exist"}, status=status.HTTP_204_NO_CONTENT)
        if check_password(password,user.password):
             return Response({"id":user.id,
                             "username":user.username,
                             "email":user.email,
                             "is_active":user.is_active,
                             "is_superuser":user.is_superuser,
                             "token":user.token}, status=status.HTTP_200_OK)
        return Response({"error":"wrong password"}, status=status.HTTP_201_CREATED)
#####################################################################
class UserLogout(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    #renderer_classes = (UserJSONRenderer,)
    def get(self, request):
        return Response({"message": "logout successful!"},status=status.HTTP_200_OK)
#####################################################################
class UserRU(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrAdmin,)
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
