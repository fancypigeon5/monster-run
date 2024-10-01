from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Equipment, EquipmentType


def equipment(request):
    equipments = Equipment.objects.filter(owner=request.user)
    equipment_types_owned = []
    print(equipments)
    for eq in equipments:
        if eq.type.name not in equipment_types_owned:
            equipment_types_owned.append(eq.type.name)
    print(equipment_types_owned)
    equipment_types = EquipmentType.objects.exclude(name__in=equipment_types_owned)
    return render(
        request,
        'equipment/equipment.html',
        {
            'equipments': equipments,
            'equipment_types': equipment_types,
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