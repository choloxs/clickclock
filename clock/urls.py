from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register_race, name="register_race"),
    path('clock', views.clock, name="clock"),
]
