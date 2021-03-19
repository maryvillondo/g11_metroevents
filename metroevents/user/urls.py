from django.urls import path
from . import views

app_name = 'user'
urlpatterns = {
	path('index_user', views.UserIndexView.as_view(), name = 'index_user_view'),
	path('events_user', views.UserEventView.as_view(), name = 'events_user_view'),
	path('profile_user', views.UserProfileView.as_view(), name = 'profile_user_view'),
}