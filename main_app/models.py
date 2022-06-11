from django.db import models
from django.contrib.auth.models import User
from django.forms import URLInput




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
    goal_description = models.CharField(max_length=500)
    avatar_img = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="profiles", default='1')
    status_img = models.CharField(max_length=500,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToCXRtr20DkXHw0BW6034Mz1JihWvkDhGcPg&usqp=CAU')

    

    def __str__(self):
        return self.name




class Post(models.Model):

    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="post", default='1')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="post", default='1')
    
    
    
   
    def __str__(self):
        return self.text

    class Meta:
        ordering = ['text']



class Comment(models.Model):
    text = models.TextField(max_length=500)
    name = models.CharField(max_length=80, default='mary')
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", default='1')
   
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.name)

    class Meta:
        ordering = ['date']
