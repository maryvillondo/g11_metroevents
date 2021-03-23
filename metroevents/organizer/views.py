from django.shortcuts import render
from django.views.generic import View
from guest.models import currentUser, Users, Organizers, Administrators
from administrator.models import Notifications
from .forms import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class OrganizerIndexView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user
		}
		return render(request, 'index_organizer.html', context)

class OrganizerEventView(View):
	def get(self, request):
		events = Events.objects.all()
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user,
			'events': events
		}
		return render(request, 'events_organizer.html', context)

class OrganizerProfileView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user
		}
		return render(request, 'profile_organizer.html', context)

class CreateEventView(View):
	def get(self, request):
		return render(request, 'create_event.html')

	def post(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		for user in user:
			user_id = user.id

		form = EventForm(request.POST)
		participants = request.POST.get("event_participants")
		print(participants)

		if form.is_valid():
			name = request.POST.get("event_name")
			date = request.POST.get("event_date")

			form = Events(event_name = name, event_date = date, num_participants = participants, user_id = user_id)
			form.save()

			return HttpResponseRedirect("http://127.0.0.1:8000/organizer/events_organizer")
		else:
			print(form.errors)
			return HttpResponse("not valid")

class NotifOrgView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)
		notifs = Notifications.objects.raw('SELECT * FROM notif, currentUser WHERE notif.receiver_id = currentUser.user_id')
		administrators = Administrators.objects.all()
		organizers = Organizers.objects.all()

		for notif in notifs:
			for administrator in administrators:
				if administrator.users_ptr_id == notif.sender_id:
					notif.sender_id = "Administrator"
			
			for organizer in organizers:
				if organizer.users_ptr_id == notif.sender_id:
					notif.sender_id = "Organizer"

		context = {
			'user' : user,
			'notifs' : notifs,
			'organizers' : organizers,
			'administrators' : administrators
		}
		return render(request, 'notif_organizer.html', context)