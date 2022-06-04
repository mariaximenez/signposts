from django.urls import path
from . import views


urlpatterns = [
    path('', views.Login.as_view(), name="login"),
    path('users/', views.UserList.as_view(), name="user_list"), 
]