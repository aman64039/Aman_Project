from django import forms
from .models import *






class UserMForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'