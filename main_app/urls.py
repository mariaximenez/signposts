from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileList.as_view(), name="profile_list"),
    path('profiles/', views.ProfileList.as_view(), name="profile_list"), 
    path('groups/', views.GroupList.as_view(), name="group_list"),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail"),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name="group_detail"),
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile_update"),
    path('profiles/<int:pk>/delete/', views.ProfileDelete.as_view(), name="profile_delete"),
    path('groups/<int:pk>/update/', views.GroupUpdate.as_view(), name="group_update"),
    path('groups/<int:pk>/delete/', views.GroupDelete.as_view(), name="group_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('myprofile/', views.MyProfileDetail.as_view(), name="myprofile_detail"),
    path('mygroup/', views.MyGroupPost.as_view(), name="mygroup_post"),

]