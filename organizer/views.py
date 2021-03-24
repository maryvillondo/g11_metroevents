from django.shortcuts import render
from django.views.generic import View
from guest.models import currentUser, Users, Organizers, Administrators
from administrator.models import Notifications
from user.models import Participants
from .forms import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class OrganizerIndexView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)
		events = Events.objects.raw('SELECT * FROM me_events WHERE me_events.id IN (SELECT participants.event_id FROM participants, currentUser WHERE participants.user_id = currentUser.user_id)')
		ownedEvents = Events.objects.raw('SELECT * FROM me_events WHERE me_events.id IN (SELECT me_events.id FROM me_events, currentUser WHERE me_events.user_id = currentUser.user_id)')
		
		context = {
			'user' : user,
			'events' : events,
			'owned' : ownedEvents
		}
		return render(request, 'index_organizer.html', context)
	
	def post(self,request):
		if request.method == 'POST':
			if 'btnLeave' in request.POST:
				current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
				event_id = request.POST.get("event_id")
				participant = Participants.objects.filter(event_id = event_id, user_id = current).delete()
				print('Left Successfully')
			elif 'btnCancel' in request.POST:
				event_id = request.POST.get("mine_id")
				cancel_event = Events.objects.filter(id = event_id).delete()
				print('Cancelled Successful')
		return HttpResponseRedirect("http://127.0.0.1:8000/organizer/index_organizer")

class OrganizerEventView(View):
	def get(self, request):
		events = Events.objects.raw('SELECT * FROM me_events WHERE me_events.id NOT IN (SELECT participants.event_id FROM participants, currentUser WHERE participants.user_id = currentUser.user_id)')
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user,
			'events': events
		}
		return render(request, 'events_organizer.html', context)

	def post(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		for user in user:
			user_id = user.id

		if request.method == 'POST':
			if 'btnJoin' in request.POST:
				event_id = request.POST.get("event_id")
				str_nump = request.POST.get("event_nump")
				event_numparticipants = int(str_nump) + 1

				update_numparticipants = Events.objects.filter(id = event_id).update(num_participants = event_numparticipants)

				print(update_numparticipants)
				print('Number of Participans Updated')

				form = Participants(event_id = event_id, user_id = user_id)
				form.save()
			elif 'btnInterested' in request.POST:
				event_id = request.POST.get("event_id1")	
				str_numi = request.POST.get("event_numi")
				event_numinterested = int(str_numi)

				update_numinterested = Events.objects.filter(id = event_id).update(num_interested = event_numinterested+1)

				print(update_numinterested)
				print('Number of Interested Updated')
		return HttpResponseRedirect("http://127.0.0.1:8000/organizer/events_organizer")

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