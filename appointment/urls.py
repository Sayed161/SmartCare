from django.urls import path,include
from rest_framework import routers
from .views import Appointment_ViewSet

router = routers.DefaultRouter()
router.register("",Appointment_ViewSet)

urlpatterns = [
    path("",include(router.urls))
]
