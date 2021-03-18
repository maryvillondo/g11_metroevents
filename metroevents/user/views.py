from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class UserIndexView(View):
	def get(self, request):
		return render(request, 'index.html')

class UserRegisterView(View):
	def get(self, request):
		return render(request, 'register.html')

class UserEventView(View):
	def get(self, request):
		return render(request, 'events.html')