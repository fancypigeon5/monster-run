from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from monster.models import Monster

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
        return render(
            request,
            'arena/battleground.html',
            {
                'monster': monster
            }
        )
    else:
        messages.add_message(
                request, messages.ERROR,
                'something went wrong'
            )
        return HttpResponseRedirect(reverse('arena'))