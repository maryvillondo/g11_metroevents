from django.shortcuts import render
from django.views.generic import View
from guest.models import currentUser, Users, Organizers, Administrators
from user.models import Requests
from organizer.models import Events
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

class AdminIndexView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user
		}
		return render(request, 'index_admin.html', context)

class AdminEventView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)
		events = Events.objects.all()

		context = {
			'user' : user,
			'events' : events
		}
		return render(request, 'events_admin.html', context)

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

				return HttpResponseRedirect("http://127.0.0.1:8000/administrator/requests_admin")

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

				return HttpResponseRedirect("http://127.0.0.1:8000/administrator/requests_admin")
