from django.urls import path
from . import views

app_name = 'user'
urlpatterns = {
	path('index_organizer', views.OrganizerIndexView.as_view(), name = 'index_organizer_view'),
	path('events_organizer', views.OrganizerEventView.as_view(), name = 'events_organizer_view'),
	path('profile_organizer', views.OrganizerProfileView.as_view(), name = 'profile_organizer_view'),
}