from django.urls import path, include
from . import views 
from django.contrib.auth.views import LoginView


urlpatterns = [
   path('signup', views.signup, name="signup"),
   path('', include('django.contrib.auth.urls')),
   path('login/', LoginView.as_view(), name='login'),
]