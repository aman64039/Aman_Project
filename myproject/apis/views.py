from django.shortcuts import render
from rest_framework import viewsets
from website.models import *
from rest_framework.views import APIView
from django.conf import settings
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import AllowAny , IsAuthenticated
from .serializers import *
from rest_framework import status
from rest_framework.response import Response


class CoursesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

#now define the url 
class CreateCourses(APIView):
	def get(self,request,*args,**kwargs):
		resp = {}
		datalist = []
		data = Courses.objects.all()
		if data:
			for i in data:
				dataobj = {}
				dataobj["name"] = i.name
				datalist.append(dataobj)
			resp["message"] = "success"
			resp["data"] = datalist
			return Response(resp, status = status.HTTP_200_OK)
		else:
			resp["data"] = None
			resp["message"] = "No History"
			return Response(resp, status = status.HTTP_404_NOT_FOUND) 



class CreateCoursesApi(APIView):
	model = User
	permission_classes = (IsAuthenticated,)
	def get_object(self):
		obj = self.request.user
		return obj

	def post(self,request,*args,**kwargs):
		user = self.get_object()
		if user:
			resp = {}
			name = request.data.get('name')
			data = Courses.objects.filter(name=name.upper()).first()
			if not data:
				course = Courses(name = name.upper())
				course.save()
				resp["message"] = "success"
				resp["name"] = name
				return Response(resp,status = status.HTTP_201_CREATED)
			else:
				resp["message"] = "Already Exists"
				return Response(resp,status =status.HTTP_400_BAD_REQUEST)


class AdminLogin(APIView):
	def post(self,request,*args,**kwargs):
		resp = {}
		email = request.data.get('email')
		password = request.data.get('password')
		user =  User.objects.filter(email=email).first()
		if user and user.check_password(password):
			payload = api_settings.JWT_PAYLOAD_HANDLER(user)
			jwt_token = api_settings.JWT_ENCODE_HANDLER(payload)
			resp["message"] = "User Logged in "
			resp["access_token"] = jwt_token
		return Response(resp , status = status.HTTP_200_OK)
