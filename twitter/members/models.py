from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pass
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.user.username