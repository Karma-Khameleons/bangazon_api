from rest_framework import serializers
from api.models import Order
class OrderSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates Customer Order Serializer
    @rtwhitfield84
    """

    class Meta:
      model = Order
      fields = ('active', 'customer', 'payment_type', 'products', )