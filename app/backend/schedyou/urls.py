from django.urls import path
from schedyou import views

urlpatterns = [
    path("", views.home, name="home"),
]
