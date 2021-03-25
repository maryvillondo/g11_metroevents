from django.urls import path
from . import views

#path arranged alphabetically by name
app_name= 'guest'
urlpatterns=[
    #path('api/data', views.get_data, name='api-data'),

    #TEST URL
    path('events', views.GuestEventView.as_view(), name='events_view'),
    path('', views.GuestIndexView.as_view(), name='index_view'),
	path('register', views.GuestRegisterView.as_view(), name='register_view'),
    path('error', views.GuestErrorView.as_view(), name='error_view')
]