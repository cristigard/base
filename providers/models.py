from django.db import models
from users.models import CustomUser




class ServiceArea(models.Model):
	provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	polygon_name = models.CharField(max_length = 100) 
	price = models.CharField(max_length = 100)
	coordinates = models.CharField(max_length = 700)
	

	def __str__(self):
		return  f'{self.coordinates}, {self.polygon_name}, {self.provider}, {self.price}'