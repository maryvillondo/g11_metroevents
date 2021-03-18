from django.urls import path
from . import views

app_name = 'user'
urlpatterns = {
	path('index', views.UserIndexView.as_view(), name = 'index_view'),
	path('register', views.UserRegisterView.as_view(), name = 'register_view'),
	path('events', views.UserEventView.as_view(), name = 'events_view'),
}