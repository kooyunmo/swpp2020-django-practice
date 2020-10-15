from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero

# Create your views here.
def index(request):
  return HttpResponse('Hello, World!')

def hero_id(request, id=0):
  return HttpResponse('Your id is ' + str(id) + '!')

def hero_name(request, name=""):
  return HttpResponse('Your name is ' + str(name) + '!')

def intoduce():
  return HttpResponse('Hello, my name is ' + str(name) + ' and my score is ' + str(score) + '!')

@csrf_exempt
def hero_list(request):
  if request.method == 'GET':
    hero_all_list = [hero for hero in Hero.objects.all().values()]
    return JsonResponse(hero_all_list, safe=False)
  elif request.method == 'POST':
    try:
      body = request.body.decode()
      hero_name = json.loads(body)['name']
    except (KeyError) as e:
      return HttpResponseBadRequest()
    hero = Hero(name=hero_name)
    hero.save()
    response_dict = {'id': hero.id, 'name': hero.name}
    return JsonResponse(response_dict, status=201)
  else:
    return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id):
  if request.method == 'GET':
    hero_found = Hero.objects.filter(id=id)
    if hero_found.exists():
      hero_dict = {'id':hero_found[0].id, 'name':hero_found[0].name, 'age':hero_found[0].age}
      return JsonResponse(hero_dict)
    else:
      return HttpResponseBadRequest()
  elif request.method == 'PUT':
    try:
      body = request.body.decode()
      hero_ = json.loads(body)
    except (KeyError) as e:
      return HttpResponseBadRequest()
    hero_name = hero_['name']
    hero_age = hero_['age']
    hero = Hero(name=hero_name, age=hero_age)
    hero.save()
    hero_dict = {'id':hero.id, 'name':hero.name, 'age':hero.age}
    return JsonResponse(hero_dict, status=201)
  else:
    return HttpResponseNotAllowed(['GET', 'PUT'])