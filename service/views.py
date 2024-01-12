from django.shortcuts import render
from rest_framework import viewsets
from . models import Service
from . serializers import Service_Serializer
# Create your views here.

class Service_Viewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = Service_Serializer
# Create your views here.
