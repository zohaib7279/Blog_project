from django.shortcuts import render
from rest_framework import viewsets
from main_app.models import User , Role
from main_app.serializers import UserSerializer , RoleSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer