from django.urls import path
from . import views


urlpatterns = [
    path('', views.Login.as_view(), name="login"),
    # path('signup/'), views.Signup.as_view(), name="signup"),
    # path('profile/'), views.Profile.as_view(), name='profile'),
    # path('post/'), views.Post.as_view(), name = "posts"),
]