from django import forms
from .models import *

class UserForm(forms.ModelForm):
	
	class Meta:
		model = Users
		fields = ('firstName','lastName', 'user_pword', 'email')

# class LoginForm(forms.ModelForm):

# 	class Meta:
# 		model = Login
# 		fields = ('emailAddress', 'password')