from django.db import models
from django.contrib.auth.models import User




class Group(models.Model):

    name = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    goal_img = models.CharField(max_length=500)
   
 
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']






class Profile(models.Model):

    name = models.CharField(max_length=150)
    badge_num= models.IntegerField(default=0)
    goal_description = models.CharField(max_length=500, default='1')
    avatar_img = models.CharField(max_length=500,default='1')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="profiles", default='1')
   

    def __str__(self):
        return self.name


class Post(models.Model):

    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group", default='1')
   
    
    
   
    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']



class Comment(models.Model):
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts", default='1')
   
  
    
    
    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']
