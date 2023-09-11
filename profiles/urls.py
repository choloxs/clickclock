from . import views
from django.urls import path

urlpatterns = [
    path('', views.register_profile, name="register_profile"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
]