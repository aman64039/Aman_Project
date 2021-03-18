from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from website.models import *
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import ListView
# Create your views here.

#functions base views 
#abc
def index(request):
	print(request)
	print(dir(request))
	print("My name is Aman")
	print(request.get_full_path())
	return HttpResponse("Aman")

def name(request):
	response = HttpResponse()
	# response.write("<h1>this is my response <h1>")
	print(response.status_code)
	response.write("<h1>Page not Found<h1>")
	response.write("<h1>404<h1>")
	response.status_code = 400
	return response

def getdetails(request):
	data = Student.objects.all()#orm
	return render(request , 'account/listview.html',{'data':data})

def create_view(request):
	if request.method == "POST":
		name = request.POST.get('name')
		age = request.POST['age']
		obj = Student(name=name,age = age)
		obj.save()
		return HttpResponse("Done")
	return render(request , 'account/createview.html')


def create_view_form(request):
	form = StudentForm()
	if request.method == "POST":
		print("hy")
		form = StudentForm(request.POST)
		if form.is_valid():
			print("Hello 2 ")
			cd = form.cleaned_data
			print(cd)
			std = Student(name=cd["name"],age=cd["age"])
			std.save()
			return HttpResponse("Done ")

	return render(request, 'account/create_view_form.html',{'form':form})



def create_view_modelform(request):
	form = StudentMForm()
	if request.method == "POST":
		print("hy")
		form = StudentMForm(request.POST)
		if form.is_valid():
			print("Hello 2 ")
			form.save()
			# cd = form.cleaned_data
			# print(cd)
			# std = Student(name=cd["name"],age=cd["age"])
			# std.save()
			return HttpResponse("Done ")

	return render(request, 'account/create_view_form.html',{'form':form})


def updateview(request,id=None):
	data = Student.objects.filter(id = id).first()
	form = StudentMForm(request.POST or None,instance = data)
	if form.is_valid():
		fm = form.save()
		fm.save()
		return HttpResponseRedirect(reverse('data'))
	return render(request,'account/update.html',{'form':form})



@login_required()
def amanview(request):
	message = "Hey This is Aman I am super user "
	return render(request , 'account/amanview.html',{'msg':message})


def amanlogin(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('view'))
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username = username,password = password)
		if user:
			if user.is_superuser:
				auth.login(request,user)
				return HttpResponseRedirect(reverse('admindashboard'))
			auth.login(request,user)
			return HttpResponseRedirect(reverse('view'))
		else:
			messages.error(request, 'Invalid Credentials')

	return render(request , 'account/amanlogin.html')

def signupview(request):
	if request.method == "POST":
		email = request.POST["email"]
		password = request.POST.get('password')
		password1 = request.POST.get('password1')
		print(email,password,password1)
		if password == password1:
			user = User.objects.create_user(username=email,email=email,password=password)
			user.save()
			student = StudentDetails()
			student.student = user
			student.studentname = "studentname"
			student.save()
		else:
			messages.error(request, 'Password Dosent Match')

	return render(request,'account/signup.html')
#usercreation form----- avaible (all filed)
#model form of user (forms.py --- create a form , User , -- fields )

# UserCreationForm
def signup_form(request):
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('login'))
	form = UserCreationForm()
	return render(request, 'account/signup_form.html',{'form':form})


def signup_customform(request):
	form = SignupForm()
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('login'))
	form = SignupForm()
	return render(request, 'account/signup_customform.html',{'form':form})



"""
email = request.POST['email']
or 
email = request.POST.get('email')

User.objects.filter(email = email).delete()


"""

class Someview(View):
	def get(self,request):
		data = request.GET.get("name")
		print(data)
		return HttpResponse("This is my first class based view get method ")

	def post(self,request):
		name = request.POST.get('name')
		age = request.POST['age']
		


class StudentList(ListView):
	model = Student