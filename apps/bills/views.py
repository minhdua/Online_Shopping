from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Bill
from .serializers import BillSerializer
from rest_framework.response import Response
import django_filters.rest_framework as filters
class BillListCreate(generics.ListCreateAPIView):
    """
        function: List all categories in the database
               or Create and add a category to the database
        permissions:Admin -> create and list
                    Other -> list
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'
#############################################################################
class BillRUD(generics.RetrieveUpdateDestroyAPIView):
    """
        function: Retrieve, update, delete specific Category
        permisson: admin -> governor, other -> read only
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (IsAuthenticated,)
