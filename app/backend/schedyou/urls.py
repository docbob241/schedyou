from django.urls import path
from schedyou import views

urlpatterns = [
    path("", views.home, name="home"),
    path("schedyou/<name>", views.hello_there, name="hello_there"),

]
