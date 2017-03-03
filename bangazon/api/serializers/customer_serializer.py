from rest_framework import serializers
from api.models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Customer Model.
    @rtwhitfield84
    """
    class Meta:
        model = Customer
        fields = '__all__'