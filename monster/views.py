from django.shortcuts import render, get_object_or_404, redirect
from .models import Monster, MonsterType
from .forms import MonsterForm
from equipment.models import Equipment

# Create your views here.

def monster(request):
    if request.user.is_authenticated:
        monsters = Monster.objects.filter(owner=request.user)
        if monsters is None:
            return redirect("create_monster")
        else:
            for monster in monsters:
                equipped = monster.equipped.all()
                max_health = monster.type.base_max_health
                damage = monster.type.base_damage
                for item in equipped:
                    max_health += item.type.benefit_health
                    damage += item.type.benefit_damage
                if monster.health == monster.max_health:
                    monster.health = max_health
                monster.max_health = max_health
                monster.damage = damage
                monster.save()
            equipped = Equipment.objects.filter(owner=request.user).exclude(monster=None)
            return render(
                request,
                "monster/monster.html",
                {
                    "monsters": monsters,
                    "equipped": equipped,    
                },
            ) 
    else:
        return render(
                request,
                "monster/monster.html",
            ) 

def create_monster(request):
    if request.method == "POST":
            monster_form = MonsterForm(data=request.POST)
            monster_type = get_object_or_404(MonsterType, id=request.POST.get("type"))
            if monster_form.is_valid():
                new_monster = monster_form.save(commit=False)
                new_monster.owner = request.user
                new_monster.max_health = monster_type.base_max_health
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