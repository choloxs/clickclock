from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),
    path('clock/', include('clock.urls')),
    path('codes', include('codes.urls')),
    path('profiles/', include('django.contrib.auth.urls')),
    path('profiles/', include('profiles.urls')),
    path('race', include('race.urls')),
]

