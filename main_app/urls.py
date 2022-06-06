from django.urls import path
from . import views


urlpatterns = [
    path('', views.Login.as_view(), name="login"),
    path('users/', views.UserList.as_view(), name="user_list"), 
    path('groups/', views.GroupList.as_view(), name="group_list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name="group_detail"),
    path('users/<int:pk>/update/', views.UserUpdate.as_view(), name="user_update"),
    path('users/<int:pk>/delete/', views.UserDelete.as_view(), name="user_delete"),
    path('groups/<int:pk>/update/', views.GroupUpdate.as_view(), name="group_update"),
    path('groups/<int:pk>/delete/', views.GroupDelete.as_view(), name="group_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")


]