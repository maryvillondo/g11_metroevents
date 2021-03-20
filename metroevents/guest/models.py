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