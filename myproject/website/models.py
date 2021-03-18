from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid




class User(AbstractUser):
	# username = models.CharField(max_length=30, unique)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	email = models.EmailField(unique=True)
	created_date = models.DateTimeField(auto_now_add=True,null= True)
	details_filled = models.BooleanField(default = False)
	user_type_choices = [('student','student'),('trainer','trainer')]
	user_type = models.CharField(max_length = 250 ,choices = user_type_choices, default='student')


class StudentDetails(models.Model):
	student = models.OneToOneField(User, on_delete=models.CASCADE)
	studentname = models.CharField(max_length = 250 , null = True,blank = True)
	created_date = models.DateTimeField(auto_now_add=True,null= True)

class TrainerDetails(models.Model):
	trainer = models.OneToOneField(User, on_delete=models.CASCADE)
	trainername = models.CharField(max_length = 250 , null = True,blank = True)
	charges = models.FloatField(null = True , blank = True)
	created_date = models.DateTimeField(auto_now_add=True,null= True)

class Courses(models.Model):
	name = models.CharField(max_length = 250 , null = True,blank = True)

class StudentEnroled(models.Model):
	trainer = models.ForeignKey(TrainerDetails, on_delete=models.CASCADE,related_name="student")
	student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE,related_name="trainer")
	course = models.ForeignKey(Courses, on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add=True,null= True)




