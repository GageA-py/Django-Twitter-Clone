from django.db import models
from django.contrib.auth.models import User
from members.models import Profile

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, 
    related_name="tweets", on_delete=models.DO_NOTHING)
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} {self.body} ({self.created_at:%H:%M}): "


