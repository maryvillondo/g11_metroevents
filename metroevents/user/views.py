from django.shortcuts import render
from django.views.generic import View
from guest.models import currentUser, Users

# Create your views here.

class UserIndexView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 2)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user
		}

		return render(request, 'index_user.html', context)

class UserEventView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 2)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user
		}
		return render(request, 'events_user.html', context)

class UserProfileView(View):
	def get(self, request):
		current = currentUser.objects.values_list("user_id", flat=True).get(pk = 2)
		user = Users.objects.filter(id = current)

		context = {
			'user' : user
		}
		return render(request, 'profile_user.html', context)