from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero
from json import JSONDecodeError

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()] 
        return JsonResponse(hero_all_list, safe=False)

    elif request.method == 'POST': 
        try:
            body = request.body.decode()
            hero_name = json.loads(body)["name"] 
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero_age} 
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def hero_name(request, name=""):
    return HttpResponse('Your name is '+name+'\n')


def hero_id(request, id=3):
    return HttpResponse('Your id is '+str(id)+'\n')


@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        targetHero = Hero.objects.all().values().get(id=id)
        print(targetHero)
        return JsonResponse(targetHero, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)["name"] 
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero_list = Hero.objects.all()
        targetHero = Hero.objects.all().get(id=id)
        targetHero.name = hero_name
        targetHero.age = hero_age
        targetHero.save()
        print(targetHero)
        response_dict = {'id': targetHero.id, 'name': targetHero.name, 'age': targetHero.age} 
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])