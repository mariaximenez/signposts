from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import User as UserModel
from .models import Group as GroupModel





class Login(TemplateView):
     template_name = "login.html"



# class Signup(TemplateView):
#      template_name = "signup.html"




class UserList(TemplateView):
    template_name = "user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = UserModel.objects.all() 
        return context


class GroupList(TemplateView):
    template_name = "group_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = GroupModel.objects.all() 
        return context




class Post(TemplateView):
     template_name = "posts.html"