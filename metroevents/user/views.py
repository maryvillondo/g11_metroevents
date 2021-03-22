from django.shortcuts import render
from django.views.generic import View
from guest.models import currentUser, Users
from organizer.models import Events
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.

class UserIndexView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user
		}

		return render(request, 'index_user.html', context)

class UserEventView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 1)
		user = Users.objects.filter(id = current)
		events = Events.objects.all()

		context = {
			'user' : user,
			'events' : events
		}
		return render(request, 'events_user.html', context)

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


