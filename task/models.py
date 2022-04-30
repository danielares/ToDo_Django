from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    creation_date = models.DateField(auto_now=True)
    due_date =models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    lated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'user'