from django.urls import path
from . import views

app_name = 'user'
urlpatterns = {
	path('index', views.GuestIndexView.as_view(), name = 'index'),
	path('events', views.GuestEventView.as_view(), name = 'events'),
	path('register', views.GuestRegisterView.as_view(), name = 'register'),
}