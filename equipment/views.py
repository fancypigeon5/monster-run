from django.shortcuts import render
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
