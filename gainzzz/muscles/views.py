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

