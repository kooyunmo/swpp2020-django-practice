from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.http import HttpResponse
import json

from json import JSONDecodeError

from .models import Hero

def index(request):
    return HttpResponse('Hello, world!')

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False) 
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
            hero_score = json.loads(body)['score']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age, 'score': hero.score}
        return JsonResponse(response_dict, status=201) 
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id=None, score=0):
    if request.method == 'GET':
        hero = [hr for hr in Hero.objects.filter(id=id).values()]
        return JsonResponse(hero, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
            hero_score = json.loads(body)['score'] == None ? 0 : json.loads(body)['score']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(id = id, name=hero_name, age=hero_age, score=hero_score)
        hero.save()
        response_dict = {'id': id, 'name': hero.name, 'age': hero.age, 'score': hero.score}
        return JsonResponse(response_dict, status=201) 
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

def hero_name(request, name=""):
    return HttpResponse('Your name is ' + name + '!')
def hero_id(request, id=None):
    return HttpResponse('Your id is ' + str(id) + '!')