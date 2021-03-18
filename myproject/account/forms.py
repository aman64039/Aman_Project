from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.Form):
	name = forms.CharField(label='Your name')
	age = forms.IntegerField(label='Your age')



class StudentMForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

class SignupForm(UserCreationForm):
	first_name = forms.CharField(max_length = 250,required = False,help_text="Optional")
	last_name = forms.CharField(max_length = 250,required = False,help_text="Optional")
	class Meta:
		model = User
		fields = ('username','first_name','last_name','password1','password2')
