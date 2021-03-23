from django.db import models
from datetime import datetime
from guest.models import Users

# Create your models here.
class Events(models.Model):
	user = models.ForeignKey(Users, null = False, blank = False, on_delete = models.CASCADE, related_name = "Events_Users")
	event_name = models.CharField(max_length = 50, null = True, blank = True)
	event_date = models.DateField()
	num_participants = models.IntegerField(null = True, blank = True)
	num_interested = models.IntegerField(default = 1, null = True, blank = True)

	class Meta:
		db_table = "me_events"