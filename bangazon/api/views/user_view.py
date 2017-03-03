from django.contrib.auth.models import User
from django.shortcuts import render
from api import serializers, models
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    Creates StaffView
    @asimonia
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return serializers.UserSerializer
        return serializers.RestrictedUserSerializer 