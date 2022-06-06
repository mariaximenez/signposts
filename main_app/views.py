from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import User as User
from .models import Group as GroupModel
from .models import Profile as ProfileModel
from .models import Post as PostModel
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator





class ProfileList(TemplateView):
    template_name = "profile_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profiles"] = ProfileModel.objects.all() 
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


class ProfileDetail(DetailView):
    model = ProfileModel
    template_name = "profile_detail.html"


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

class ProfileUpdate(UpdateView):
    model = ProfileModel
    fields = ['name', 'badge_num', 'goal_description','avatar_img', 'user']
    template_name = "profile_update.html"


    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})
 

class ProfileDelete(DeleteView):
    model = ProfileModel
    template_name = "profile_delete_confirmation.html"
    success_url = "/profiles/"

@method_decorator(login_required, name='dispatch')
class MyProfilePost(TemplateView):
    template_name = "myprofile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = PostModel.objects.all() 
        return context




@method_decorator(login_required, name='dispatch')
class MyProfileDetail(TemplateView):
    template_name = "myprofile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        name = self.request.GET.get("name")
        context["profile"] = ProfileModel.objects.filter(user=self.request.user)
        return context



@method_decorator(login_required, name='dispatch')
class MyGroupDetail(TemplateView):
    template_name = "mygroup_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        name = self.request.GET.get("name")
        context["profile"] = ProfileModel.objects.filter(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class MyGroupPost(TemplateView):
    template_name = "mygroup_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = PostModel.objects.all() 
        return context





class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
