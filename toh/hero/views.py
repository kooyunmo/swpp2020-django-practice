from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero

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
    except (KeyError, JSONDecodeError) as e:
      return HttpResponseBadRequest()
    hero = Hero(name=hero_name, age=hero_age)
    hero.save()
    response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
    return JsonResponse(response_dict, status=201)
  else:
    return HttpResponseNotAllowed(['GET', 'POST']) 


def index(request):
  return HttpResponse('Hello, world!')


@csrf_exempt
def hero_info(request, id):
  if request.method == 'GET':
    try:
      selected_hero = Hero.objects.get(id=id)
    except (Exception):
      return HttpResponse('Hero not Found!')
    response_dict = {'id': selected_hero.id, 'name': selected_hero.name, 'age': selected_hero.age}
    return JsonResponse(response_dict, status=201)

  elif request.method == 'PUT':
    try:
      selected_hero = Hero.objects.get(id=id)
    except (Exception):
      return HttpResponse('Hero not Found!')
    try:
      body = request.body.decode()
      hero_name = json.loads(body)['name']
      hero_age = json.loads(body)['age']
    except (KeyError, JSONDecodeError) as e:
      return HttpResponseBadRequest()
    hero = selected_hero
    hero.name = hero_name
    hero.age = hero_age
    hero.save()
    response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
    return JsonResponse(response_dict, status=201)
  
  else:
    return HttpResponseNotAllowed(['GET', 'PUT']) 


def id_view(request, id):
  return HttpResponse('Your id is %d!' % id)


def name_view(request, name):
  return HttpResponse('Your name is %s!' % name)

