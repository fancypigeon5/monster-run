from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Equipment, EquipmentType
from .forms import EquipForm, EquipmentTypeForm
from monster.models import Monster


@login_required
def equipment(request):
    """Display the user's equipment and provide options to equip items.

    Args:
        request: HttpRequest: The HTTP request object.

    Returns:
        equipment.html: A rendered template displaying the user's equipment, 
            available equipment types, and the ability to equip items.
    """

    equipments = Equipment.objects.filter(owner=request.user)
    equipment_types = EquipmentType.objects.all()
    equip_form = EquipForm()
    equip_form.fields['monster'].queryset = Monster.objects.filter(
        owner=request.user)
    monsters = Monster.objects.filter(owner=request.user).all
    return render(
        request,
        'equipment/equipment.html',
        {
            'monsters': monsters,
            'equipments': equipments,
            'equipment_types': equipment_types,
            'equip_form': equip_form,
        }
    )


@login_required
def equipment_create(request, equipment_type_id):
    """Create a new equipment item for the user.

    Args:
        request: HttpRequest: The HTTP request object.
        equipment_type_id: int: The ID of the equipment type to create.

    Returns:
        Redirect: A redirect response to the equipment page after creating the equipment.

    Raises:
        Http404: If the equipment type does not exist.

    Adds:
        A success message indicating that the user should start running to unlock their new equipment.
    """

    equipment_type = get_object_or_404(EquipmentType, id=equipment_type_id)
    new_equipment = Equipment(owner=request.user, type=equipment_type)
    new_equipment.save()
    messages.add_message(
        request, messages.SUCCESS,
        'Start running to unlock your new equipment'
    )
    return HttpResponseRedirect(reverse('equipment'))


@login_required
def equip_to(request, equipment_id):
    """Equip an item to a specified monster.

    Args:
        request: HttpRequest: The HTTP request object.
        equipment_id: int: The ID of the equipment to be equipped.

    Returns:
        Redirect: A redirect response to the equipment page after equipping the item.

    Raises:
        Http404: If the monster or equipment does not exist or does not belong to the user.

    Adds:
        A success message indicating that the item has been equipped.
    """

    if request.method == 'POST':
        monster = get_object_or_404(
            Monster, pk=request.POST['monster'], owner=request.user)
        equipment = get_object_or_404(
            Equipment, pk=equipment_id, owner=request.user)
        equipped = monster.equipped.filter(
            type__category=equipment.type.category)
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


@login_required
def unequip(request, equipment_id):
    """Unequip an item from a monster.

    Args:
        request: HttpRequest: The HTTP request object.
        equipment_id: int: The ID of the equipment to be unequipped.

    Returns:
        Redirect: A redirect response to the equipment page after unequipping the item.

    Raises:
        Http404: If the equipment does not exist or does not belong to the user.

    Adds:
        A success message indicating that the item has been unequipped.
    """

    equipment = get_object_or_404(
        Equipment, pk=equipment_id, owner=request.user)
    equipment.monster = None
    equipment.save()
    messages.add_message(
        request, messages.SUCCESS,
        'Item unequipped'
    )
    return HttpResponseRedirect(reverse('equipment'))


@login_required
def unlock(request, equipment_id):
    """Unlock an equipment item for the user.

    Args:
        request: HttpRequest: The HTTP request object.
        equipment_id: int: The ID of the equipment to be unlocked.

    Returns:
        Redirect: A redirect response to the equipment page after attempting to unlock the item.

    Raises:
        Http404: If the equipment does not exist or does not belong to the user.

    Adds:
        An error message if the item is already unlocked, or a success message if it is newly unlocked.
    """

    equipment = get_object_or_404(
        Equipment, pk=equipment_id, owner=request.user)
    if equipment.unlocked:
        messages.add_message(
            request, messages.ERROR,
            'Item already unlocked'
        )
    else:
        equipment.unlocked = True
        equipment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'New equipment unlocked'
        )
    return HttpResponseRedirect(reverse('equipment'))

@staff_member_required
def add_equipment_type(request):
    """Create a new equipment type.

    Args:
        request: HttpRequest: The HTTP request object.

    Returns:
        Redirect: A redirect response to the equipment page after creating the equipment type.

    Adds:
        A success message indicating that the equipment type has been created.
    """
    equipment_type_form = EquipmentTypeForm()
    if request.method == "POST":
        equipment_type_form = EquipmentTypeForm(data=request.POST)
        if equipment_type_form.is_valid():
            new_equipment = equipment_type_form.save(commit=False)
            new_equipment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'New equipment type created'
            )
            return HttpResponseRedirect(reverse('equipment'))
    return render(
        request,
        "equipment/new-equipment-type.html",
        {
            "equipment_type_form": equipment_type_form,
        },
    )

@staff_member_required
def edit_or_delete_type(request):
    """Display all equipment types.

    Args:
        request: HttpRequest: The HTTP request object.

    Returns:
        edit-equipment-type.html: A rendered template displaying all equipment types.
    """
    equipment_types = EquipmentType.objects.all()
    return render(
        request,
        "equipment/edit-or-delete-type.html",
        {
            "equipment_types": equipment_types,
        },
    )
    

@staff_member_required
def edit_equipment_type(request, equipment_type_id):
    """Edit an equipment type.

    Args:
        request: HttpRequest: The HTTP request object.

    Returns:
        Redirect: A redirect response to the equipment page after editing the equipment type.

    Adds:
        A success message indicating that the equipment type has been edited.
    """

    equipment_type = get_object_or_404(EquipmentType, id=equipment_type_id)
    equipment_type_form = EquipmentTypeForm(instance=equipment_type)
    if request.method == "POST":
        equipment_type_form = EquipmentTypeForm(data=request.POST, instance=equipment_type)
        if equipment_type_form.is_valid():
            equipment_type = equipment_type_form.save(commit=False)
            equipment_type.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Equipment type edited'
            )
            return HttpResponseRedirect(reverse('equipment'))
    return render(
        request,
        "equipment/edit-equipment-type.html",
        {
            "equipment_type_form": equipment_type_form,
        },
    )

@staff_member_required
def delete_equipment_type(request, equipment_type_id):
    """Delete an equipment type.

    Args:
        request: HttpRequest: The HTTP request object.

    Returns:
        Redirect: A redirect response to the equipment page after deleting the equipment type.

    Adds:
        A success message indicating that the equipment type has been deleted.
    """

    equipment_type = get_object_or_404(EquipmentType, id=equipment_type_id)
    equipment_type.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'Equipment type deleted'
    )
    return HttpResponseRedirect(reverse('equipment'))    
    