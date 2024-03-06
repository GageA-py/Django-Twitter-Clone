from django.contrib import admin
from .models import ToDoList, Item
from tweets.models import Tweet

# Register your models here.
admin.site.register(Tweet)
