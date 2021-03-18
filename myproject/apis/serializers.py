from django.contrib.auth.models import User, Group
from rest_framework import serializers
from website.models import *


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Courses
		fields = ['name']



# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']