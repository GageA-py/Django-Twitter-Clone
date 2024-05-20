from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.home, name='home'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("show_tweet/<int:pk>", views.show_tweet, name="show_tweet"),
    path("delete_tweet/<int:pk>", views.delete_tweet, name="delete_tweet")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

