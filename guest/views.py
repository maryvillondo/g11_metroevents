from django.shortcuts import render, redirect
from django.views.generic import View
from organizer.models import Events
from .forms import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class GuestIndexView(View):
	def get(self, request):
		return render(request,'index.html')

	def post(self, request):
		form = LoginForm(request.POST)

		if form.is_valid():
			email = request.POST.get("email")
			pword = request.POST.get("pword")

			# user = authenticate(request, email = email, password = pword)

			# if user is not None:
			# 	print('Found')
			# 	login(request, user)
			# 	currentUser = user
			# 	print(str(currentUser.id) + "is logged in")
			# 	context = {
			# 	'currentUser' : currentUser
			# 	}

			users = Users.objects.all()
			organizers = Organizers.objects.all()
			administrators = Administrators.objects.all()

			for administrator in administrators:
				for user in users:
					if (administrator.users_ptr_id == user.id):
						if (user.email == email and user.user_pword == pword):
							form = currentUser.objects.get(id=1)
							form.user_id = user.id
							form.save()
							return HttpResponseRedirect("https://group11-metroevents.azurewebsites.net/administrator/index_admin")

			for organizer in organizers:
				for user in users:
					if (organizer.users_ptr_id == user.id):
						if (user.email == email and user.user_pword == pword):
							form = currentUser.objects.get(id=1)
							form.user_id = user.id
							form.save()
							return HttpResponseRedirect("https://group11-metroevents.azurewebsites.net/organizer/index_organizer")

			for user in users:
				if (user.email == email and user.user_pword == pword):
					form = currentUser.objects.get(id=1)
					form.user_id = user.id
					form.save()
					return HttpResponseRedirect("https://group11-metroevents.azurewebsites.net/user/index_user")
		else:
			return HttpResponseRedirect("https://group11-metroevents.azurewebsites.net/error")

class GuestEventView(View):
	def get(self, request):
		events = Events.objects.all()

		context = {
			'events' : events
		}
		return render(request,'events.html', context)

class GuestRegisterView(View):
	def get(self, request):
		return render(request,'register.html')

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
				# user = User.objects.create_user(first, email, pword)
				# user.last_name = last
				# user.save()
				return HttpResponseRedirect("https://group11-metroevents.azurewebsites.net")
			else:
				return HttpResponseRedirect("https://group11-metroevents.azurewebsites.net/error")
		else:
			print(form.errors)
			return HttpResponseRedirect('https://group11-metroevents.azurewebsites.net/error')

class GuestErrorView(View):
	def get(self, request):
			return render(request,'wrongCredentials.html')