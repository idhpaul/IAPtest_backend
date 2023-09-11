from django.contrib.auth.models import User
from rest_framework import serializers

from IAP.models import Purchace

class PurchaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchace
        fields = ['id', 'source', 'product_id', 'purchase_id', 
                  'localverificationdata', 'serververificationdata',
                  'purchace_date','purchace_price']