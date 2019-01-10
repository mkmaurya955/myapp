from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class TempHumdity(models.Model):
	max_temperature= models.IntegerField()
	min_temperature= models.IntegerField()
	max_humidity   = models.IntegerField()
	min_humidity   = models.IntegerField()



	class Meta:
		ordering=['max_temperature']





