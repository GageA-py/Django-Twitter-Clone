from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from members.models import Profile
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
    tweets = Tweet.objects.all().order_by("-created_at") 
    if request.user.is_authenticated:
        form = TweetForm(request.POST or None)
        tweets = Tweet.objects.all().order_by("-created_at")

        if request.method == "POST":
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect('dashboard')

        profiles = Profile.objects.all()
        return render(request, 'main/dashboard.html', {"tweets":tweets, "form":form, "profiles":profiles})
    else:
        
        return render(request, 'main/dashboard.html', {"tweets":tweets})

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        tweets = Tweet.objects.filter(user_id=pk)

        return render(request, 'main/profile.html', {"profile": profile, "tweets": tweets})
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('login')

