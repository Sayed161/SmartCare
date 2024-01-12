from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . views import Contact_us_Viewset

router = DefaultRouter()
router.register('',Contact_us_Viewset)
urlpatterns = [
    path('',include(router.urls))
]
