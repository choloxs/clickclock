from django import forms
from django.shortcuts import render, redirect
from .models import Race
from clock.forms import Roll
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from math import radians, cos, sin, asin, sqrt


def haversine(lat1, lon1, lat2, lon2):
    radius = 6372.8  # For Earth radius in kilometers use 6372.8 km
    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))
    return radius * c


# Create your views here.
def race(request):
    submitted = False
    user = request.user
    if user.is_authenticated and user.username == 'admin':
        if request.method == "POST":
            race_id = request.POST['race']
            roll = Roll.objects.filter(race=race_id)
            this_race = Race.objects.filter(race_id=race_id)
            if roll and this_race:
                for obj in roll:
                    distance = haversine(this_race[0].latitude, this_race[0].longitude, obj.loft.latitude, obj.loft.longitude)
                    obj.distance = distance
                    obj.save()
                return HttpResponseRedirect('race?submitted=True')
            else:
                messages.success(request, "Race not found!")
        else:
            if 'submitted' in request.GET:
                submitted = True
        return render(request, 'update.html', {"submitted": submitted})

    else:
        messages.success(request, "Please login as administrator!")
        return redirect('login')






