from django.shortcuts import render
from rest_framework import viewsets,filters,pagination
from . models import Designation,Specialization,Doctor,AvailableTime,Review
from . serializers import Doctor_Serializer,Specialization_Serializer,AvailableTime_Serializer,Designation_Serializer,Review_Serializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class Doctor_pagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 50

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

class Doctor_Viewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = Doctor_Serializer
    filter_backends = [filters.SearchFilter]
    pagination_class = Doctor_pagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']
    
class Specialization_Viewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = Specialization_Serializer

class Designation_Viewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = Designation_Serializer

class AvailableTime_Viewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTime_Serializer
    filter_backends = [AvailableTimeForSpecificDoctor]


class Review_Viewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = Review_Serializer