from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class UserIndexView(View):
	def get(self, request):
		return render(request, 'index_user.html')

class UserEventView(View):
	def get(self, request):
		return render(request, 'events_user.html')

class UserProfileView(View):
	def get(self, request):
		return render(request, 'profile_user.html')