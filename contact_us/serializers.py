from rest_framework import serializers
from . import models
class Contact_us_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact_us
        fields = '__all__'