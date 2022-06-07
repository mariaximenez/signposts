from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Profile, User as User
from .models import Group as GroupModel
from .models import Profile as ProfileModel
from .models import Post as PostModel
from .forms import CommentForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import F


class Home(TemplateView):
        template_name="home.html"




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
    fields = ['name', 'badge_num', 'goal_description', 'avatar_img', 'group']
    template_name = "profile_update.html"

    def get_success_url(self):
        return reverse('myprofile_detail', kwargs={'pk': self.object.pk})


class ProfileDelete(DeleteView):
    model = ProfileModel
    template_name = "profile_delete_confirmation.html"
    success_url = "/myprofile/"


@method_decorator(login_required, name='dispatch')
class MyProfileDetail(TemplateView):
    template_name = "myprofile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["profile"] = ProfileModel.objects.filter(
            user=self.request.user)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = PostModel.objects.all()
        return context



class ProfileCreate(CreateView):
    model = ProfileModel
    fields = ['name', 'goal_description', 'avatar_img', 'user','group']
    template_name = "profile_create.html"
    success_url = "/groups/"

    # def get_success_url(self):
    #     return reverse('profile_detail', {'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class MyGroupPost(TemplateView):
    template_name = "group_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = PostModel.objects.filter(group=context['pk'])
        return context




class PostCreate(CreateView):
    model = PostModel
    fields = ['text', 'group']
    template_name = "post_create.html"

    def get_success_url(self):
        return reverse('group_detail', kwargs={'pk': self.object.pk})


class PostUpdate(UpdateView):
    model = PostModel
    fields = ['text']
    template_name = "post_update.html"
    success_url = "/groups/"

    # def get_success_url(self):
    #     return reverse('group_detail', kwargs={'pk': self.object.pk})


class PostDelete(DeleteView):
    model = PostModel
    template_name = "post_delete_confirmation.html"
    success_url = "/groups/"




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
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
