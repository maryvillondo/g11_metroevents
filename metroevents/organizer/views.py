from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class OrganizerIndexView(View):
	def get(self, request):
		return render(request, 'index_organizer.html')

class OrganizerEventView(View):
	def get(self, request):
		return render(request, 'events_organizer.html')

class OrganizerProfileView(View):
	def get(self, request):
		return render(request, 'profile_organizer.html')