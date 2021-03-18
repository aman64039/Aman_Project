import re
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def validation_email(value):
	regex = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
	match = re.match(regex , value)
	if match is None:
		raise ValidationError("not a valid email")
	else:
		return value

class Student(models.Model):
	course_list = [
	('python','Python'),
	('django','Python Django'),
	('js','JavaScript')]
	name = models.CharField(max_length = 150,null = True , blank = True)
	age = models.CharField(max_length = 15)
	contact = models.CharField(max_length=20, null = True, blank = True)
	active = models.BooleanField(default = True)
	course = models.CharField(max_length = 250 ,choices = course_list, null = True)
	# email = models.EmailField(unique = True)
	email = models.CharField(max_length=150, validators=[validation_email], null = True)

	def __str__(self):
		return self.name

