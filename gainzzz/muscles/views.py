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


@csrf_exempt
def all_muscles(request):
    muscles = Muscle.objects.values('name', 'description')
    response = JsonResponse(dict(muscles=list(muscles)))
    response['Access-Control-Allow-Origin'] = "*"
    return response


@csrf_exempt
def muscle(request, muscle_id=0):
    muscle_group = Muscle.objects.get(id=muscle_id)
    muscle_dict = dict(name=muscle_group.name, description=muscle_group.description, image=muscle_group.image)

    exercises = Exercises.objects.filter(muscle_id=muscle_id)
    exercise_list = list()
    for e in exercises:
        exercise_list.append(dict(name=e.name, description=e.description, image=e.image))

    stretches = Stretches.objects.filter(muscle_id=muscle_id)
    stretches_list = list()
    for s in stretches:
        stretches_list.append(dict(name=s.name, description=s.description, image=s.image))

    injuries = Injuries.objects.filter(muscle_id=muscle_id)
    injuries_list = list()
    for i in injuries:
        injuries_list.append(dict(name=i.name, description=i.description, image=i.image))

    response = JsonResponse(dict(muscle=muscle_dict,
                                 exercises=exercise_list,
                                 stretches=stretches_list,
                                 injuries=injuries_list))
    response['Access-Control-Allow-Origin'] = "*"
    return response


@csrf_exempt
def muscle_name(request, name=None):
    muscle_group = Muscle.objects.get(name=name)
    muscle_dict = dict(id=muscle_group.id)

    response = JsonResponse(muscle_dict)
    response['Access-Control-Allow-Origin'] = "*"
    return response


@csrf_exempt
def add_exercise(request):
    req = json.loads(request.body)
    exerc = Exercises(name=req.name, description=req.description, image=req.image)
    exerc.save()
    return HttpResponse("OK")
