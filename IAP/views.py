from rest_framework import generics

from IAP.models import Purchace, User
from IAP.serializers import PurchaceSerializer, UserSerializer

class PurchaceList(generics.ListCreateAPIView):
    queryset = Purchace.objects.all()
    serializer_class = PurchaceSerializer


class PurchaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchace.objects.all()
    serializer_class = PurchaceSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer