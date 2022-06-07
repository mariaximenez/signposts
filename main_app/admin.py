from django.contrib import admin
from .models import Group, Profile, Post, Comment


admin.site.register(Group) 
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)

