from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Monster, MonsterType
from .forms import MonsterForm
from equipment.models import Equipment


@login_required
def monster(request):
    """Display a list of monsters owned by the user.

    Args:
        request: HttpRequest: The HTTP request object.

    Returns:
        monster.html: A template displaying the user's monsters and equipped items.

    Redirects:
        If the user has no monsters, redirects to the "create_monster" view.

    Updates:
        Calculates and updates the max health and damage for each monster based on equipped items.
    """

    monsters = Monster.objects.filter(owner=request.user).all()
    if monsters.first() is None:
        return redirect("create_monster")
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
    equipped = Equipment.objects.filter(
        owner=request.user).exclude(monster=None)
    return render(
        request,
        "monster/monster.html",
        {
            "monsters": monsters,
            "equipped": equipped,
        },
    )


@login_required
def create_monster(request):
    """Create a new monster for the user.

    Args:
        request: HttpRequest: The HTTP request object.

    Returns:
        create_monster.html: A rendered template for monster creation with the form or 
            redirects to the home page if the form is successfully submitted.

    Raises:
        ValidationError: If the submitted form data is invalid.
    """

    monster_form = MonsterForm()
    if request.method == "POST":
        monster_form = MonsterForm(data=request.POST)
        if monster_form.is_valid():
            new_monster = monster_form.save(commit=False)
            new_monster.owner = request.user
            new_monster.max_health = new_monster.type.base_max_health
            new_monster.health = new_monster.type.base_max_health
            new_monster.damage = new_monster.type.base_damage
            new_monster.save()
            return redirect("home")
    return render(
        request,
        "monster/create_monster.html",
        {
            "monster_form": monster_form,
        },
    )
