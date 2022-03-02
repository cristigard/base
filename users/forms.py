from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ['surname','last_name','phone_number', 'email', 'language', 'currency','password1', 'password2']