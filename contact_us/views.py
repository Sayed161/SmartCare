from django.shortcuts import render
from rest_framework import viewsets
from . models import Contact_us
from . serializers import Contact_us_Serializer
# Create your views here.

class Contact_us_Viewset(viewsets.ModelViewSet):
    queryset = Contact_us.objects.all()
    serializer_class = Contact_us_Serializer