from django.urls import path
from . import views

app_name = 'organizer'
urlpatterns = {
	path('index_organizer', views.OrganizerIndexView.as_view(), name = 'index_organizer_view'),
	path('events_organizer', views.OrganizerEventView.as_view(), name = 'events_organizer_view'),
	path('profile_organizer', views.OrganizerProfileView.as_view(), name = 'profile_organizer_view'),
	path('create_event', views.CreateEventView.as_view(), name = 'create_event_view'),
	path('notif_organizer', views.NotifOrgView.as_view(), name = 'notif_organizer_view')
}