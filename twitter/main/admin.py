from django.contrib import admin
from tweets.models import Tweet
from members.models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Profile)



class ProfileInline(admin.StackedInline):  # or admin.TabularInline for a more compact display
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)