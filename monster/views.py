from django.shortcuts import render

# Create your views here.

def monster(request):
    return render(
        request,
        "monster/monster.html",
    ) 