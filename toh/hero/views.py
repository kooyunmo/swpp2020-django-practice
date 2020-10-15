from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero


def index(request):
    return HttpResponse('Hello world!')

@csrf_exempt
def readInt(request, int=0):
    return HttpResponse('Your id is ' + str(int))

@csrf_exempt
def readStr(request, string=0):
    return HttpResponse('Your name is ' + string)

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        print(Hero.objects.all().values())
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
        except (KeyError, json.JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def hero_info(request, heroId=0):
    print(heroId)
    if request.method == 'GET':
        searched_hero_list = [hero for hero in Hero.objects.all().values() if hero['id'] == heroId]
        if len(searched_hero_list) > 0:
            return JsonResponse(searched_hero_list[0], safe=False)
        else:
            return HttpResponseBadRequest()
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            new_hero = json.loads(body)
            newHero = Hero.objects.get(id=heroId)
            newHero.name = new_hero['name']
            newHero.age = new_hero['age']
            newHero.save()
        except (KeyError, json.JSONDecodeError) as e:
            return HttpResponseBadRequest()
        searched_hero_list = [hero for hero in Hero.objects.all().values() if hero['id'] == heroId]
        if len(searched_hero_list) > 0:
            return JsonResponse(searched_hero_list[0], safe=False)
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
