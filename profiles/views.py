from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import RegForm
from .models import RegProfile, LoftProfile
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from decimal import Decimal


class PasswordChanged(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    messages.success(request, "Password change successfully!")
    return redirect('home_page')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.success(request, "Loft Id or Password is invalid")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out!")
    return redirect('home_page')


# Create your views here.
def register_profile(request):
    submitted = False
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            registration = form.save()
            #user = RegProfile.objects.filter(mobile_number=registration.mobile_number)
            #user1 = LoftProfile.objects.filter(mobile_number=registration.mobile_number)
            #registration.save()
            messages.success(request, "Registration was successful! Wait for administrator to measure your coordinates.")
            return redirect('register_profile')
    else:
        form = RegForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "registration.html", {"form": form, "submitted": submitted})


def register_loft(request):
    submitted = False
    registry = RegProfile.objects.values_list('loft_name')
    registry_list = list(registry)
    if request.method == "POST":
        loft = request.POST.get('loft', False)
        latitude = request.POST.get('latitude', False)
        longitude = request.POST.get('longitude', False)
        if loft and latitude and longitude:
            registration = RegProfile.objects.filter(loft_name=loft)
            loft_ids = User.objects.values_list('username', flat=True)
            max_id = int(registration[0].zip_code + '001')
            for user_id in loft_ids:
                if registration[0].zip_code in loft_ids[0]:
                    current_id = int(loft_ids[0])
                    if current_id > max_id:
                        max_id = current_id
            user_number = max_id + 1
            username = str(user_number)
            password = username+registration[0].last_name
            user = User.objects.create(username=username, password=password)
            user.email = registration[0].email
            user.first_name = registration[0].first_name
            user.last_name = registration[0].last_name
            user.save()

            loft_id = User.objects.get(username=username)
            loft_name = loft
            mobile_number = registration[0].mobile_number
            latitude = Decimal(latitude)
            longitude = Decimal(longitude)
            loft = LoftProfile.objects.create(loft_id=loft_id, loft_name=loft_name, mobile_number=mobile_number)
            loft.latitude = latitude
            loft.longitude = longitude
            loft.save()
            messages.success(request, loft)
            return HttpResponseRedirect('register_loft?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "register_loft.html", {"registry": registry_list, "submitted": submitted})


