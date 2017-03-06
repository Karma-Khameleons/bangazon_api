from rest_framework import serializers
from api.models import PaymentType


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates PaymentType Serializer
    @rtwhitfield84
    """
    class Meta:
        model = PaymentType
        fields = ('id', 'customer', 'card_type', 'billing_name',
        'card_number','expiration_date', 'cvv', 'url')