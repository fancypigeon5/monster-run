from django.shortcuts import render, get_object_or_404, redirect
from .models import Monster, MonsterType
from .forms import MonsterForm

# Create your views here.

def monster(request):
    if request.user.is_authenticated:
        monster = Monster.objects.filter(owner=request.user).first()
        if monster is None:
            return redirect("create monster")
        else:
            return render(
                request,
                "monster/monster.html",
                {"monster": monster},
            ) 
    else:
        return render(
                request,
                "monster/monster.html",
            ) 

def create_monster(request):
    if request.method == "POST":
            monster_form = MonsterForm(data=request.POST)
            print('Creating monster')
            monster_type = get_object_or_404(MonsterType, id=request.POST.get("type"))
            if monster_form.is_valid():
                new_monster = monster_form.save(commit=False)
                new_monster.owner = request.user
                new_monster.health = monster_type.base_max_health
                new_monster.damage = monster_type.base_damage
                new_monster.save()
                return redirect("home")
    else:
        monster_form = MonsterForm()
        return render(
            request,
            "monster/create_monster.html",
            {
                "monster_form": monster_form,
            },
        )