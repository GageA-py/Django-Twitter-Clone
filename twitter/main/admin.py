from django.contrib import admin
from .models import ToDoList, Item
from tweets.models import Tweet
from members.models import Profile

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Profile)