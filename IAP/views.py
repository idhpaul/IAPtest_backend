from rest_framework import generics

from IAP.models import Purchace
from IAP.serializers import PurchaceSerializer

class PurchaceList(generics.ListCreateAPIView):
    queryset = Purchace.objects.all()
    serializer_class = PurchaceSerializer


class PurchaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchace.objects.all()
    serializer_class = PurchaceSerializer