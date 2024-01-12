from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . views import Service_Viewset

router = DefaultRouter()
router.register('',Service_Viewset)
urlpatterns = [
    path('',include(router.urls))
]
