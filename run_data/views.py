from django.shortcuts import render, reverse, get_object_or_404
from django.db.models import F
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import RunData
from .forms import UnlockRunDataForm, RecoverRunDataForm
from equipment.models import Equipment
from monster.models import Monster

# Create your views here.
def run(request):
    runs = RunData.objects.filter(user=request.user).order_by('-created_on')
    unlock_run_form = UnlockRunDataForm()
    unlock_run_form.fields['equipment'].queryset = Equipment.objects.filter(owner=request.user).exclude(unlocked=True)
    recover_run_form = RecoverRunDataForm()
    recover_run_form.fields['monster'].queryset = Monster.objects.filter(owner=request.user).exclude(health=F('max_health'))
    return render(
        request,
        'run_data/run_data.html',
        {
            'runs': runs,
            'unlock_run_form': unlock_run_form,
            'recover_run_form': recover_run_form,
        }
    )

def enter_run(request, choice):
    if request.method == "POST":
        if choice == "unlock":
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

def delete_run(request, run_data_id):
    run_data = get_object_or_404(RunData, pk=run_data_id)
    run_data.delete()
    messages.add_message(
        request, messages.SUCCESS,
        'run successfully deleted'
    )
    return HttpResponseRedirect(reverse('run_data'))