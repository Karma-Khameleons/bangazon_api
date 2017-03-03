from django.contrib.auth.models import User
from django.shortcuts import render
from api import serializers, models
from rest_framework import viewsets

class LineItemViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Line Items to be viewed or edited.
    @samphillips1879

    """

    queryset = models.LineItem.objects.all()
    serializer_class = serializers.LineItemSerializer