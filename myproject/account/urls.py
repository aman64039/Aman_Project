"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', index),
    path('name', name),
    path('data', getdetails,name = 'data'),
    path('create_view', create_view),
    path('create_view_form',create_view_form),
    path('create_view_modelform',create_view_modelform),
    path('edit/<int:id>',updateview),
    path('amanview',amanview,name='view'),
    path('login',amanlogin,name = 'login'),
    path('logout',auth_views.LogoutView.as_view(template_name="account/amanlogin.html"),name = 'logout'),
    path('signupview',signupview,name = 'signupview'),
    path('signup_form',signup_form,name = 'signup_form'),
    path('signup_customform',signup_customform,name = 'signup_customform'),
    path('firstview',Someview.as_view(),name = 'firstview'),
    path('firstlistview',StudentList.as_view(),name = 'firstlistview'),
    path('abcview',TemplateView.as_view(template_name="account/dummy.html"),name = 'firstlistview'),




]
