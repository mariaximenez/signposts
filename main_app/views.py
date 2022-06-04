from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import User as UserModel





class Login(TemplateView):
     template_name = "login.html"



# class Signup(TemplateView):
#      template_name = "signup.html"


class User:
    def __init__(self, first_name, last_name, username, password, goal_description, avatar_img):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.goal_description= goal_description
        self.avatar_img = avatar_img


class UserList(TemplateView):
    template_name = "user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = UserModel.objects.all() 
        return context




class Post(TemplateView):
     template_name = "posts.html"