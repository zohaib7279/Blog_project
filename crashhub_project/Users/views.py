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
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

class UserCreate(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"msg": "User created"})
        return Response(serializer.errors)