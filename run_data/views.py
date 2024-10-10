from django.shortcuts import render, reverse, get_object_or_404
from django.db.models import F
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import RunData
from .forms import UnlockRunDataForm, RecoverRunDataForm
from equipment.models import Equipment
from monster.models import Monster


@login_required
def run(request):
    """Display the user's run data and form for adding a new run.

    Args:
        request: HttpRequest: The HTTP request object.

    Returns:
        Run_data.html: A rendered template displaying the user's run data and 
            a form to enter running data.
    """
    runs = RunData.objects.filter(user=request.user).order_by('-created_on')
    unlock_run_form = UnlockRunDataForm()
    unlock_run_form.fields['equipment'].queryset = Equipment.objects.filter(
        owner=request.user).exclude(unlocked=True)
    recover_run_form = RecoverRunDataForm()
    recover_run_form.fields['monster'].queryset = Monster.objects.filter(
        owner=request.user).exclude(health=F('max_health'))
    equipments = Equipment.objects.filter(owner=request.user, unlocked=False)
    monsters = Monster.objects.filter(
        owner=request.user).exclude(health=F('max_health'))
    return render(
        request,
        'run_data/run_data.html',
        {
            'runs': runs,
            'equipments': equipments,
            'monsters': monsters,
            'unlock_run_form': unlock_run_form,
            'recover_run_form': recover_run_form,
        }
    )


@login_required
def enter_run(request, choice):
    """Process a user's run entry for unlocking equipment or recovering a monster.

    Args:
        request: HttpRequest: The HTTP request object.
        choice: str: The action to perform, either "unlock" or "recover".

    Returns:
        Redirect: A redirect response to the run data page after processing the entry.

    Raises:
        ValidationError: If the submitted form data is invalid or conditions are not met.

    Adds:
        A success message if progress is added to equipment or recovery is applied to a monster.
        An error message if no equipment is available to unlock or no monsters require recovery.
    """

    if request.method == "POST":
        monsters = Monster.objects.filter(
            owner=request.user).exclude(health=F('max_health'))
        equipment = Equipment.objects.filter(
            owner=request.user, unlocked=False)
        if choice == "unlock":
            if equipment.first() is None:
                messages.add_message(
                    request, messages.ERROR,
                    'Choose an equipment to unlock first'
                )
                return HttpResponseRedirect(reverse('run_data'))
            unlock_run_form = UnlockRunDataForm(data=request.POST)
            if unlock_run_form.is_valid():
                new_run = unlock_run_form.save(commit=False)
                new_run.user = request.user
                new_run.save()
                equipment = new_run.equipment
                equipment.progress += new_run.distance
                equipment.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Progress added to equipment'
                )
        elif choice == "recover":
            if monsters.first() is None:
                messages.add_message(
                    request, messages.ERROR,
                    'You have no monsters that are in need of recovery'
                )
                return HttpResponseRedirect(reverse('run_data'))
            recover_run_form = RecoverRunDataForm(data=request.POST)
            if recover_run_form.is_valid():
                new_run = recover_run_form.save(commit=False)
                new_run.user = request.user
                new_run.save()
                monster = new_run.monster
                monster.health += (new_run.distance * 10)
                if monster.health > monster.max_health:
                    monster.health = monster.max_health
                monster.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'recovery added to monster'
                )

    return HttpResponseRedirect(reverse('run_data'))


@login_required
def delete_run(request, run_data_id):
    """Delete a run entry and update associated monster or equipment.

    Args:
        request: HttpRequest: The HTTP request object.
        run_data_id: int: The ID of the run data to be deleted.

    Returns:
        Redirect: A redirect response to the run data page after deletion.

    Raises:
        Http404: If the run data does not exist or does not belong to the user.

    Adds:
        A success message indicating that the run was successfully deleted.
    """

    run_data = get_object_or_404(RunData, pk=run_data_id, user=request.user)
    if run_data.monster:
        monster = run_data.monster
        monster.health -= (run_data.distance*10)
        if monster.health <= 0:
            monster.health = 0
        monster.save()
    elif run_data.equipment:
        equipment = run_data.equipment
        equipment.progress -= run_data.distance
        if equipment.progress < equipment.type.distance_needed:
            if equipment.monster:
                equipment.monster = None
            equipment.unlocked = False
        equipment.save()
    run_data.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'run successfully deleted'
    )
    return HttpResponseRedirect(reverse('run_data'))
