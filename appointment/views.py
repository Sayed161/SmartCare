from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import Appointment_Serializer
# Create your views here.
class Appointment_ViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = Appointment_Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset