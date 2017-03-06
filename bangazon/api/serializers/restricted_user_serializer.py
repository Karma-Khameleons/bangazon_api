from django.contrib.auth.models import User
from rest_framework import serializers

class RestrictedUserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked Serializer for the Customer Model.
    @rtwhitfield84
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'url')
