from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Login(TemplateView):
     template_name = "login.html"



# class Signup(TemplateView):
#      template_name = "signup.html"


class Profile(TemplateView):
     template_name = "profile.html"



class Post(TemplateView):
     template_name = "posts.html"