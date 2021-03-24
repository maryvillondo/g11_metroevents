from django.shortcuts import render
from django.views.generic import View
from guest.models import currentUser, Users, Organizers, Administrators
from user.models import Requests, Participants
from organizer.models import Events
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

class AdminIndexView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)
		allUsers = Users.objects.raw('SELECT * FROM users')
		events = Events.objects.raw('SELECT * FROM me_events WHERE me_events.id IN (SELECT participants.event_id FROM participants, currentUser WHERE participants.user_id = currentUser.user_id)')
		allEvents = Events.objects.raw('SELECT * FROM me_events')

		context = {
			'user' : user,
			'allUsers' : allUsers,
			'events' : events,
			'allEvents' : allEvents
		}
		return render(request, 'index_admin.html', context)
	
	def post(self,request):
		if request.method == 'POST':
			if 'btnLeave' in request.POST:
				current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
				event_id = request.POST.get("event_id")
				participant = Participants.objects.filter(event_id = event_id, user_id = current).delete()
				print('Delete Successful')
			elif 'btnCancel' in request.POST:
				event_id = request.POST.get("alle_id")
				cancel_event = Events.objects.filter(id = event_id).delete()
				print('Cancelled Successful')
		return render(request, 'index_admin.html')

class AdminEventView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)
		events = Events.objects.raw('SELECT * FROM me_events WHERE me_events.id NOT IN (SELECT participants.event_id FROM participants, currentUser WHERE participants.user_id = currentUser.user_id)')

		context = {
			'user' : user,
			'events' : events
		}
		return render(request, 'events_admin.html', context)

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
		return render(request, 'events_admin.html')

class AdminProfileView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user
		}
		return render(request, 'profile_admin.html', context)

class AdminRequestView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)
		users = Users.objects.all()
		requests = Requests.objects.filter(pending=1)

		context = {
			'user' : user,
			'requests': requests
		}
		return render(request, 'requests_admin.html', context)

	def post(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		for user in user:
			currentUser_id = user.id

		if request.method == 'POST':
			if 'btnAccept' in request.POST:
				req_id = request.POST.get("request-id")
				user_id = request.POST.get("user-id")
				req_type=  request.POST.get("request-type")

				users = Users.objects.all()

				for user in users:
					if (user.id == int(user_id)):
						if (req_type == 'administrator'):
							print('administrator')
							form = Administrators(users_ptr_id = user_id, firstName = user.firstName, 
								lastName = user.lastName, birthdate = user.birthdate, email = user.email, 
								user_pword = user.user_pword, register_date = user.register_date)
							form.save()

							form1 = Notifications(about = 'Your application for Account Upgrade to Administrator is granted. Welcome to the group of Administrators!',
								sender_id = currentUser_id, receiver_id = user_id)
							form1.save()
						else:
							print('organizer')
							form = Organizers(users_ptr_id = user_id, firstName = user.firstName, 
								lastName = user.lastName, birthdate = user.birthdate, email = user.email, 
								user_pword = user.user_pword, register_date = user.register_date)
							form.save()

							form1 = Notifications(about = 'Your application for Account Upgrade to Organizer is granted. Welcome to the group of Organizers!',
								sender_id = currentUser_id, receiver_id = user_id)
							form1.save()

				update_request = Requests.objects.filter(id = req_id).update(pending = 0)

				return render(request, 'requests_admin.html')

			elif 'btnDeny' in request.POST:
				req_id = request.POST.get("request-id")
				user_id = request.POST.get("user-id")
				req_type = request.POST.get("request-type")

				if req_type == 'administrator':
					form = Notifications(about = 'Your application for Account Upgrade to Administrator is denied. You can still apply for another request. Thank you!',
								sender_id = currentUser_id, receiver_id = user_id)
					form.save()
				else:
					form = Notifications(about = 'Your application for Account Upgrade to Organizer is denied. You can still apply for another request. Thank you!',
								sender_id = currentUser_id, receiver_id = user_id)
					form.save()

				update_request = Requests.objects.filter(id = req_id).update(pending = 0)

				return render(request, 'requests_admin.html')
