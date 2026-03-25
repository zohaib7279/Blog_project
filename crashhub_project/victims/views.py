from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Victim
from .serializers import VictimSerializer

class VictimViewSet(viewsets.ModelViewSet):
    queryset = Victim.objects.all()
    serializer_class = VictimSerializer