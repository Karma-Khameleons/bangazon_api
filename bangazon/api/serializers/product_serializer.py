from rest_framework import serializers
from api.models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Product Model.
    @rtwhitfield84
    """
    class Meta:
        model = Product
        fields = ('seller', 'product_type', 'name',
        'description','price', 'quantity', )
