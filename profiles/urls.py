from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PasswordChanged

urlpatterns = [
    path('', views.register_profile, name="register_profile"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('password/', PasswordChanged.as_view(template_name='change_password.html'), name="password"),
    path('password_success', views.password_success, name="password_success"),
]