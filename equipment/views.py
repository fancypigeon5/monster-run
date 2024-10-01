from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Equipment, EquipmentType
from .forms import EquipForm
from monster.models import Monster


def equipment(request):
    equipments = Equipment.objects.filter(owner=request.user)
    equipment_types_owned = []
    for eq in equipments:
        if eq.type.name not in equipment_types_owned:
            equipment_types_owned.append(eq.type.name)
    equipment_types = EquipmentType.objects.exclude(name__in=equipment_types_owned)
    equip_form = EquipForm()
    equip_form.fields['monster'].queryset = Monster.objects.filter(owner=request.user)
    return render(
        request,
        'equipment/equipment.html',
        {
            'equipments': equipments,
            'equipment_types': equipment_types,
            'equip_form': equip_form,
        }
    )

def equipment_create(request, equipment_type_id):
    equipments = Equipment.objects.filter(owner=request.user, unlocked=False).count()
    if equipments >= 1:
        messages.add_message(
                request, messages.ERROR,
                'You are already unlocking an equipment'
            )
    else:
        equipment_type = get_object_or_404(EquipmentType, id=equipment_type_id)
        new_equipment = Equipment(owner=request.user, type=equipment_type)
        new_equipment.save()
        messages.add_message(
                request, messages.SUCCESS,
                'Start running to unlock your new equipment'
            )
    return HttpResponseRedirect(reverse('equipment'))

def equip_to(request, equipment_id):
    
    if request.method == 'POST':
        monster = get_object_or_404(Monster, pk=request.POST['monster'])
        equipment = get_object_or_404(Equipment, pk=equipment_id)
        equipped = monster.equipped.filter(type__category=equipment.type.category)
        print(equipped)
        equipped_count = equipped.count()
        if equipped_count >= 1:
            for item in equipped:
                item.monster = None
                item.save()
        equipment.monster = monster
        equipment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Item equipped'
        )

    return HttpResponseRedirect(reverse('equipment'))