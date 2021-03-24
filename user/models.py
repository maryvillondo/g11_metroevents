from django.db import models
from guest.models import Users
from organizer.models import Events

# Create your models here.

class Requests(models.Model):
	user = models.ForeignKey(Users, null = False, blank = False, on_delete = models.CASCADE, related_name = "Users")
	req_type = models.CharField(max_length = 20, null = True, blank = True)
	letter = models.CharField(max_length = 100, null = True, blank = True)
	pending = models.IntegerField(default = 0)

	class Meta:
		db_table = "Requests"

class Participants(models.Model):
	user = models.ForeignKey(Users, null = False, blank = False, on_delete = models.CASCADE, related_name = "Participants")
	event = models.ForeignKey(Events, null = False, blank = False, on_delete = models.CASCADE, related_name = "Events")

	class Meta:
		db_table = "Participants"