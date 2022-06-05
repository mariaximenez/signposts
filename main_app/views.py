from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import User as UserModel
from .models import Group as GroupModel
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse





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


class GroupDetail(DetailView):
    model = GroupModel
    template_name = "group_detail.html"


class UserDetail(DetailView):
    model = UserModel
    template_name = "user_detail.html"


class GroupUpdate(UpdateView):
    model = GroupModel
    fields = ['name', 'goal', 'goal_img']
    template_name = "group_update.html"


    def get_success_url(self):
        return reverse('group_detail', kwargs={'pk': self.object.pk})
 

class GroupDelete(DeleteView):
    model = GroupModel
    template_name = "group_delete_confirmation.html"
    success_url = "/groups/"

class UserUpdate(UpdateView):
    model = UserModel
    fields = ['first_name', 'last_name', 'username', 'password', 'goal_description','avatar_img', 'group']
    template_name = "user_update.html"


    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.object.pk})
 

class UserDelete(DeleteView):
    model = UserModel
    template_name = "user_delete_confirmation.html"
    success_url = "/users/"

class Post(TemplateView):
     template_name = "posts.html"