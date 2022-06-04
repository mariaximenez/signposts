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
        context["users"] = users # this is where we add the key into our context object for the view to use
        return context

users = [ 
    User ("Maria", "Jimenez", "mariaximenez", "Toby","Workout more", "https://i.pinimg.com/originals/21/e8/ab/21e8ab124a60870018c29387f190185c.png")
]




class Post(TemplateView):
     template_name = "posts.html"