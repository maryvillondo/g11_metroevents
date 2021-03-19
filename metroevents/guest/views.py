from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class GuestIndexView(View):
	def get(self, request):
		return render(request, 'index.html')

class GuestEventView(View):
	def get(self, request):
		return render(request, 'events.html')

class GuestRegisterView(View):
	def get(self, request):
		return render(request, 'register.html')