from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from .models import *
from django.http import HttpResponse

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

	def post(self, request):
			form = UserForm(request.POST)

			if form.is_valid():
				first = request.POST.get("firstName")
				last = request.POST.get("lastName")
				email = request.POST.get("email")
				bday = request.POST.get("bdate")
				pword = request.POST.get("pword")
				reg_date = request.POST.get("reg_date")

				users = Users.objects.all()
				count = 0

				for user in users:
					if(user.email == email):
						count = 1

				if (count == 0):
					form = Users(firstName = first, lastName = last, birthdate = bday, user_pword = pword, 
						register_date = reg_date, email = email)
					form.save()

					return redirect('guest:index_view')
				else:
					return HttpResponse("Email already taken.")
			else:
				print(form.errors)
				return HttpResponse('not valid')