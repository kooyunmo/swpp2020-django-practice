from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json import JSONDecodeError
from .models import Hero

"""
def index(request):
    return HttpResponse('Hello, world!')
"""
def hero_id(request, id):
    response = "Your id is %s"
    return HttpResponse(response % id)

def hero_name(request, name=""):
    return HttpResponse('Your name is ' + name)

def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        reponse_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(reponse_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

def hero_info(request, id=None):
    if request.method == 'GET':
        hero_my_list = [hero for hero in Hero.objects.filter(id=id).values()]
        return JsonResponse(hero_my_list, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
            # hero_score = json.loads(body)['score']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(id=id, name=hero_name, age=hero_age)
        hero.save()
        reponse_dict = {'id': id, 'name': hero.name, 'age': hero.age, 'score': hero.score}
        return JsonResponse(reponse_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
    