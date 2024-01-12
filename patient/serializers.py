from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class Patient_Serializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__'

class Registration_Serializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_confirmation']
    
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        password = self.validated_data['password']
        password2 = self.validated_data['password_confirmation']

        if password != password2 :
            raise serializers.ValidationError({"errors":"Password mismatch with Password Confirmation"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"errors":"Email already exists"})
        
        account = User(username=username, email=email,last_name=last_name,first_name=first_name)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    