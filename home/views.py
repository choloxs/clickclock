from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from clock.forms import Roll


def home_page(request):
    name = "Home Page"
    return render(request, "home.html", {"name": name})


def search(request):
    if request.method == "POST":
        race_id = request.POST.get('search')
        result = Roll.objects.filter(race__race_id__contains=race_id)
        if len(result) == 0:
            exist = False
            res = ''
            player = ''
        else:
            res = result.order_by("-speed")
            for obj in res:
                if obj.end_time is not None:
                    obj.end_time = obj.end_time.isoformat()
            player = str(len(res))
            exist = True
        return render(request, "search.html", {"result": res, "player": player, "exist": exist})

