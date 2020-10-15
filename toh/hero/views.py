from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero

# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')

def hero_id(request, id=0):
    return HttpResponse(f"Your id is {id} !")

def hero_name(request, name=""):
    return HttpResponse(f"Your name is {name}!")

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
        except (KeyError, JSONDecodeError) as e:
            return HttpRespenseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = hero.asdict()
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@csrf_exempt
def hero_one(request, id):
    if request.method == 'GET':
        hero = Hero.objects.get(id=id)
        return JsonResponse(hero.asdict(), safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body).get('name', None)
            hero_age = json.loads(body).get('age', None)
            hero_score = json.loads(body).get('score', None)
        except (KeyError, JSONDecodeError) as e:
            return HttpRespenseBadRequest()
        hero = Hero.objects.get(id=id)
        if hero_age is not None:
            hero.age=hero_age
        if hero_name is not None:
            hero.name = hero_name
        if hero_score is not None:
            hero.score = hero_score
        hero.save()
        response_dict = hero.asdict()
        return JsonResponse(response_dict, status=201)



