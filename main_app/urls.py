from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profiles/', views.ProfileList.as_view(), name="profile_list"), 
    path('groups/', views.GroupList.as_view(), name="group_list"),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail"),
    path('myprofile/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile_update"),
    path('myprofile/<int:pk>/delete/', views.ProfileDelete.as_view(), name="profile_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('myprofile/', views.MyProfileDetail.as_view(), name="myprofile_detail"),
    path('myprofile/<int:pk>/', views.MyProfilePost.as_view(), name="myprofile_post"),
    path('myprofile/new', views.ProfileCreate.as_view(), name="profile_create"),
    path('groups/<int:pk>/', views.MyGroupPost.as_view(), name="group_detail"),
    path('groups/<int:pk>/new', views.PostCreate.as_view(), name="post_create"),
    path('groups/<int:pk>/update/', views.PostUpdate.as_view(), name="post_update"),
    path('groups/<int:pk>/delete/', views.PostDelete.as_view(), name="post_delete"),
  

]