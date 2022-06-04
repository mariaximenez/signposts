from django.db import models




class Group(models.Model):

    name = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    goal_img = models.CharField(max_length=500)
 
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class User(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    goal_description = models.CharField(max_length=500)
    avatar_img = models.CharField(max_length=500)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="users", default='1')
  
    
    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']


