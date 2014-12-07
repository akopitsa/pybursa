from django.shortcuts import render
from Coaches.models import Coach


def coache_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coach/list.html', {'coaches': coaches})


def coach_item(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    return render(request, 'coach/item.html', {'coach': coach})
