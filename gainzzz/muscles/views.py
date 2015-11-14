from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from models import *
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the user index.")


def all_muscles(request):
    muscles = Muscle.objects.values('name', 'description')
    return JsonResponse(dict(muscles=list(muscles)))


def muscle(request, muscle_id=0):
    muscle_group = Muscle.objects.get(id=muscle_id)
    muscle_dict = dict(name=muscle_group.name, description=muscle_group.description)

    exercises = Exercises.objects.filter(muscle_id=muscle_id)
    exercise_list = list()
    for e in exercises:
        exercise_list.append(dict(name=e.name, description=e.description))

    stretches = Stretches.objects.filter(muscle_id=muscle_id)
    stretches_list = list()
    for s in stretches:
        stretches_list.append(dict(name=s.name, description=s.description))

    injuries = Injuries.objects.filter(muscle_id=muscle_id)
    injuries_list = list()
    for i in injuries:
        injuries_list.append(dict(name=i.name, description=i.description))

    return JsonResponse(dict(muscle=muscle_dict,
                             exercises=exercise_list,
                             stretches=stretches_list,
                             injuries=injuries_list))
