from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
	return render(request , 'website/index.html')


@login_required()
def admindashboard(request):
	return render(request,'website/admindashboard.html')

@login_required()
def studentlist(request):
	if request.user.is_authenticated:
		if request.user.is_superuser:
			pt = request.get_full_path()
			if 'student' in pt:
				data = StudentDetails.objects.all()
			elif 'trainer' in pt:
				data = TrainerDetails.objects.all()
			return render(request,'website/studentdetails.html',{'data':data})
