from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime
# Create your models here.

APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]

APPOINTMENT_TYPES = [
    ('Online', 'Online'),
    ('Offline', 'Offline'),

]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_types = models.CharField(max_length=70,choices=APPOINTMENT_TYPES)
    appointment_status = models.CharField(max_length=70,choices=APPOINTMENT_STATUS,default="Pending")
    symptoms = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name}"