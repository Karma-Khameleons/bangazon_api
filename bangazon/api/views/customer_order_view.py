from django.contrib.auth.models import User
from django.shortcuts import render
from api import serializers, models
from rest_framework import viewsets

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    -@asimonia
    """

    queryset = models.Order.objects.all().order_by('-customer')
    serializer_class = serializers.OrderSerializer
