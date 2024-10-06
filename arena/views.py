from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from monster.models import Monster, MonsterType
from equipment.models import Equipment, EquipmentType
import random

@login_required
def arena(request):
    monsters = Monster.objects.filter(owner=request.user)
    return render(
        request,
        'arena/arena.html',
        {
            'monsters': monsters,
        }
    )

@login_required
def battle(request):
    if request.method == "POST":
        monster = get_object_or_404(Monster, pk=request.POST['monster'], owner=request.user)
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
        turn = random.choice(['enemy','you'])
        equipped = monster.equipped.all()
        return render(
            request,
            'arena/battleground.html',
            {
                'enemy': enemy,
                'equipments': equipments,
                'equipped': equipped,
                'monster': monster,
                'turn': turn,
            }
        )
    messages.add_message(
            request, messages.ERROR,
            'something went wrong'
        )
    return HttpResponseRedirect(reverse('arena'))

@login_required
def strike(request, turn):
    if request.method == "POST":
        monster = get_object_or_404(Monster, pk=request.POST['monster'], owner=request.user)
        enemy = Monster.all_objects.filter(owner=request.user, pk=request.POST['enemy']).get()
        equipment_ids = request.POST['equipments'].split()
        equipments = []
        for id in equipment_ids:
            eq = EquipmentType.objects.filter(pk=int(id)).first()
            equipments.append(eq)
        equipped = monster.equipped.all()
        damage = int(request.POST['damage'])
        if turn == 'enemy':
            monster.health -= damage
            monster.save()
            if monster.health <= 0:
                return redirect('lost')
            turn = 'you'
        elif turn == 'you':
            enemy.health -= damage
            enemy.save()
            if enemy.health <= 0:
                monster.score += monster.health
                monster.save()
                return redirect('won', monster.health)
            turn = 'enemy'
        return render(
            request,
            'arena/battleground.html',
            {
                'enemy': enemy,
                'equipments': equipments,
                'equipped': equipped,
                'monster': monster,
                'turn': turn,
            }
        )
    messages.add_message(
            request, messages.ERROR,
            'something went wrong'
        )
    return HttpResponseRedirect(reverse('arena'))

@login_required
def lost(request):
    monsters = Monster.objects.filter(owner=request.user)
    return render(
        request,
        'arena/lost.html',
        {
            'monsters': monsters,
        }
    )

@login_required
def won(request, points):
    monsters = Monster.objects.filter(owner=request.user)
    return render(
        request,
        'arena/won.html',
        {
            'points': points,
            'monsters': monsters,
        }
    )

@login_required
def scoreboard(request):
    monsters = Monster.objects.order_by('-score')
    equipped = Equipment.objects.exclude(monster=None)
    return render(
        request,
        'arena/scoreboard.html',
        {
            'monsters': monsters,
            'equipped': equipped
        }
    )
