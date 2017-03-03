from django.contrib.auth.models import User
from django.shortcuts import render
from api import serializers, models
from rest_framework import viewsets

class ProductTypeViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Product Types to be viewed or edited.
    @rtwhitfield84

    """

    queryset = models.ProductType.objects.all().order_by('-category')
    serializer_class = serializers.ProductTypeSerializer