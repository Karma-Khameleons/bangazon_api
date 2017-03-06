from rest_framework import serializers
from api.models import LineItem

class LineItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the LineItem Model.
    @rtwhitfield84
    """
    class Meta:
        model = LineItem
        fields = ('order', 'product', 'quantity')