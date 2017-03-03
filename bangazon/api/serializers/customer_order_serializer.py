from rest_framework import serializers
from api.models import CustomerOrder

class OrderSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates Customer Order Serializer
    @rtwhitfield84
    """

    class Meta:
      model = CustomerOrder
      fields = ('active', 'customer', 'payment_type', 'products', )