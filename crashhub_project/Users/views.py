from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()