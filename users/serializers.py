from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ['tk', 'surname', 'last_name', 'phone_number', 'email' , 'language', 'currency', 'password']

