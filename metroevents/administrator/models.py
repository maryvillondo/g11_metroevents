from django.db import models
from datetime import datetime
from guest.models import Users

# Create your models here.

class Notifications(models.Model):
	about = models.CharField(max_length = 255, null = True, blank = True)
	notif_date = models.DateField(default = datetime.now())
	sender = models.ForeignKey(Users, null = False, blank = False, on_delete = models.CASCADE, related_name = "Sender_Users")
	receiver = models.ForeignKey(Users, null = False, blank = False, on_delete = models.CASCADE, related_name = "Receiver_Users")

	class Meta:
		db_table = "notif"