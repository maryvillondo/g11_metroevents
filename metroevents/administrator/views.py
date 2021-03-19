from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class AdminIndexView(View):
	def get(self, request):
		return render(request, 'index_admin.html')

class AdminEventView(View):
	def get(self, request):
		return render(request, 'events_admin.html')

class AdminProfileView(View):
	def get(self, request):
		return render(request, 'profile_admin.html')