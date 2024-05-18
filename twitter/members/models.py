from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", 
    related_name="followed_by",
    symmetrical=False,
    blank=True)

    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.profile_pic:
            # Assign a default
             default_pic_path = settings.STATIC_URL + 'members/static/images/egg.png'
        super().save(*args, **kwargs)

# Create a profile when user signs up
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile.objects.create(user=instance)
        user_profile.follows.add(user_profile)



#post_save.connect(create_profile, sender=User)
