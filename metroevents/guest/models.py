from django.db import models
from datetime import datetime

# Create your models here.

class Users(models.Model):
	firstName = models.CharField(max_length = 50, null = True, blank = True)
	lastName = models.CharField(max_length = 50, null = True, blank = True)
	birthdate = models.DateField(blank = True, null = True) 
	user_pword = models.CharField(max_length = 50, null = True, blank = True)
	register_date = models.DateField(default = datetime.now())
	email = models.CharField(max_length = 50, null = True, blank = True)

	class Meta:
		db_table = "Users"

class Organizers(Users):
	
	class Meta:
		db_table = "Organizers"

class Administrators(Users):

	class Meta:
		db_table = "Administrators"

class currentUser(models.Model):
	user_id = models.IntegerField()

	class Meta:
		db_table = "currentUser"