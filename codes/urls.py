from . import views
from django.urls import path


urlpatterns = [
    path('', views.codes, name="codes"),
]