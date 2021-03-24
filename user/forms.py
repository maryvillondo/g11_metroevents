from django import forms
from .models import *

class RequestForm(forms.ModelForm):
	
	class Meta:
		model = Requests
		fields = ('req_type',)