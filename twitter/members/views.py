from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm

# Create your views here.

def signup(response):
    if response.method == "POST":
        user_form = SignupForm(response.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')
    else:
        user_form = SignupForm()
    return render(response, 'authenticate/create_account.html', {'user_form':user_form})


def logout_user(request):
    logout(request)
    return redirect('/')

