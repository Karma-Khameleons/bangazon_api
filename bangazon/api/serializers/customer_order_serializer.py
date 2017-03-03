from rest_framework import serializers
from api.models import CustomerOrder

class OrderSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates Customer Order Serializer
    @rtwhitfield84
    """

    class Meta:
      model = CustomerOrder
      fields = ('active_order', 'customer', 'payment_type', 'line_items', )