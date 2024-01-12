from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . views import Doctor_Viewset,Specialization_Viewset,Designation_Viewset,AvailableTime_Viewset,Review_Viewset

router = DefaultRouter()
router.register('list',Doctor_Viewset)
router.register('specialization',Specialization_Viewset)
router.register('Designation',Designation_Viewset)
router.register('Availabletime',AvailableTime_Viewset)
router.register('review',Review_Viewset)
urlpatterns = [
    path('',include(router.urls))
]
