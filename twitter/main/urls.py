from django.urls import path, include

from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
]