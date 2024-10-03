from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from monster.models import Monster, MonsterType
from equipment.models import Equipment, EquipmentType
import random

def arena(request):
    monsters = Monster.objects.filter(owner=request.user)
    return render(
        request,
        'arena/arena.html',
        {
            'monsters': monsters,
        }
    )

def battle(request):
    if request.method == "POST":
        monster = get_object_or_404(Monster, pk=request.POST['monster'])
        enemy_monsters = Monster.all_objects.filter(owner=request.user, name='Enemy')
        for enemy_monster in enemy_monsters:
            enemy_monster.delete()
        monster_type = random.choice(MonsterType.objects.all())
        color = '#' + hex(random.randrange(0, 2**24))[2:]
        enemy = Monster(name="Enemy", owner=request.user, type=monster_type, color=color, health=monster_type.base_max_health, max_health=monster_type.base_max_health, damage=monster_type.base_damage)
        enemy.save()
        equipments = []
        for category in range(2):
            if random.choice([True, False]):
                equipment_type = random.choice(EquipmentType.objects.filter(category=category))
                enemy.health += equipment_type.benefit_health
                enemy.damage += equipment_type.benefit_damage
                enemy.save()
                equipments.append(equipment_type)
        turn = random.randint(0,1)
        return render(
            request,
            'arena/battleground.html',
            {
                'enemy': enemy,
                'equipments': equipments,
                'monster': monster,
                'turn': turn,
            }
        )
    else:
        messages.add_message(
                request, messages.ERROR,
                'something went wrong'
            )
        return HttpResponseRedirect(reverse('arena'))

