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
    muscle_group = Muscle.objects.filter(id=muscle_id)
    return JsonResponse(dict(muscle=muscle_group, exercises=))
