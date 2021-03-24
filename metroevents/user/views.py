from django.shortcuts import render
from django.views.generic import View
from guest.models import currentUser, Users, Organizers, Administrators
from organizer.models import Events
from administrator.models import Notifications
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.

class UserIndexView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)
		events = Events.objects.raw('SELECT * FROM me_events WHERE me_events.id IN (SELECT participants.event_id FROM participants, currentUser WHERE participants.user_id = currentUser.user_id)')
		context = {
			'user' : user ,
			'events' : events
		}

		return render(request, 'index_user.html', context)

	def post(self,request):
		if 'btnLeave' in request.POST:
			current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
			event_id = request.POST.get("event_id")
			participant = Participants.objects.filter(event_id = event_id, user_id = current).delete()
			print('Delete Successful')
		return HttpResponseRedirect("http://127.0.0.1:8000/user/index_user")

class UserEventView(View):
	def get(self, request):
		current = curreUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)
		events = Events.objects.raw('SELECT * FROM me_events WHERE me_events.id NOT IN (SELECT participants.event_id FROM participants, currentUser WHERE participants.user_id = currentUser.user_id)')

		context = {
			'user' : user,
			'events' : events,
		}
		return render(request, 'events_user.html', context)

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
		return HttpResponseRedirect("http://127.0.0.1:8000/user/events_user")

class UserProfileView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user
		}
		return render(request, 'profile_user.html', context)

class AccountUpgradeRequestView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user
		}
		return render(request, 'accUpgrade_user.html', context)

	def post(self, request):
		requests = Requests.objects.all()
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		for user in user:
			user_id = user.id

		form = RequestForm(request.POST)

		if form.is_valid():
			req_type = request.POST.get("req_type")
			letter = request.POST.get("letter")
			count = 0
			
			for request in requests:
				if (request.user_id == user_id and request.pending == 1):
					count = 1
					return HttpResponse("You have a pending request. Cannot request at the moment.")
			
			if (count == 0):
				form = Requests(req_type = req_type, letter = letter, user_id = user_id, pending = 1)
				form.save()
				return HttpResponseRedirect("http://127.0.0.1:8000/user/index_user")
		else:
			print(form.errors)
			return HttpResponse("not valid")

class UserNotifView(View):
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
		return render(request, 'notif_user.html', context)