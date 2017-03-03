from rest_framework import serializers
from api.models import ProductType

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    """
    Creates ProductType Serializer
    @rtwhitfield84
    """

    class Meta:
        model = ProductType
        fields = ('label', )