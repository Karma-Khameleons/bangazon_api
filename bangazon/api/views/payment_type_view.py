from django.contrib.auth.models import User
from django.shortcuts import render
from api import serializers, models
from rest_framework import viewsets

class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    Creates PaymentType View
    @nchemsak
    """
    queryset = models.PaymentType.objects.all()
    serializer_class = serializers.PaymentTypeSerializer
