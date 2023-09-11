from django import forms
from django.shortcuts import render, redirect
from .models import Roll
from race.models import Race
from codes.models import Code
from profiles.models import LoftProfile
from .forms import RollForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime, timezone
from decimal import Decimal
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


def register_race(request):
    submitted = False
    if request.method == "POST":
        form = RollForm(request.POST)
        if form.is_valid():
            roll = form.save(commit=False)
            user = request.user
            if user.is_authenticated:
                this_user = request.user.username
                user_id = User.objects.filter(username=this_user)
                loft_id = LoftProfile.objects.filter(loft_id=user_id[0].id)
                if loft_id:
                    roll.loft = loft_id[0]
                    key = Code.objects.filter(code=roll.code)
                    if key:
                        roll.key = key[0].key
                        roll.save()
                        Code.objects.get(code=roll.code).delete()
                        messages.success(request, f"ID: {key[0].code} was successfully registered to {this_user}.")
                        return HttpResponseRedirect('register?submitted=True')
                    else:
                        messages.success(request, "Invalid Registration Code.")
                else:
                    messages.success(request, "Please contact administrator to register your loft.")
            else:
                messages.success(request, "Please login.")
                return redirect('login')

    else:
        form = RollForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "race_registration.html", {"form": form, "submitted": submitted})


def clock(request):
    submitted = False
    if request.method == "POST":
        key = request.POST['key']
        user = request.user
        if user.is_authenticated:
            roll = Roll.objects.filter(key=key)
            if roll:
                if roll[0].loft.loft_id == user:
                    clock_time = datetime.now(timezone.utc)
                    duration = clock_time - roll[0].race.start_time
                    duration_hours = duration.total_seconds()/3600
                    for obj in roll:
                        obj.end_time = clock_time
                        obj.duration = duration_hours
                        if obj.distance is not None:
                            distance = obj.distance
                        else:
                            distance = haversine(obj.race.latitude, obj.race.longitude, obj.loft.latitude, obj.loft.longitude)
                            obj.distance = distance
                        speed = distance/duration_hours
                        obj.speed = speed
                        obj.save()
                        messages.success(request, f"Clocking for key {key} was successful!")
                        return HttpResponseRedirect('clock?submitted=True')
                    else:
                        messages.success(request, "Clocking Failed!")
                else:
                    messages.success(request, "The race code is not registered to the current user!")
            else:
                messages.success(request, "Invalid Race Code!")
        else:
            messages.success(request, "Please Login!")
            return redirect('login')
    else:
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'clock.html', {"submitted": submitted})
