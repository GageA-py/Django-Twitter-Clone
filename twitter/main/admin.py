from django.contrib import admin
from tweets.models import Tweet
from members.models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
 
admin.site.unregister(Group)
admin.site.unregister(User)


class ProfileInline(admin.StackedInline):  # or admin.TabularInline for a more compact display
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


# Extend user model 
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]


# Register your models here.
admin.site.register(Tweet)
admin.site.register(User, UserAdmin)






