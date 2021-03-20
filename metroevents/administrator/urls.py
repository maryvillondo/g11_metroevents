from django.urls import path
from . import views

app_name = 'administrator'
urlpatterns = {
	path('index_admin', views.AdminIndexView.as_view(), name = 'index_admin_view'),
	path('events_admin', views.AdminEventView.as_view(), name = 'events_admin_view'),
	path('profile_admin', views.AdminProfileView.as_view(), name = 'profile_admin_view'),
}