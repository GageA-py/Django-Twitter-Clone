from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList 
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from tweets.models import Tweet
from tweets.forms import TweetForm
from django.contrib import messages

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def dashboard(request):
    if request.user.is_authenticated:
        form = TweetForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                messages.success(request, "Your Tweet Has Been Posted!")
                return redirect('dashboard')

        tweets = Tweet.objects.all().order_by("-created_at")
        return render(request, 'main/dashboard.html', {"tweets":tweets, "form":form})
    else:
        tweets = Tweet.objects.all().order_by("-created_at")
        return render(request, 'main/dashboard.html', {"tweets":tweets})
    