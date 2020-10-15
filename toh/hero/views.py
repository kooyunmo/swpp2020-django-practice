from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero

def index(request):
  return HttpResponse('Hello, world!')

def id(request, id):
  return HttpResponse("Your id is " + str(id) + "!")

def name(request, name):
  return HttpResponse("Your name  is " + name + "!")

@csrf_exempt
def hero_list(request):
  if request.method == 'GET':
    hero_all_list = [hero for hero in Hero.objects.all().values()]
    '''
     If the safe parameter is set to False , any object can be passed for serialization;
     otherwise only dict instances are allowed
    '''
    return JsonResponse(hero_all_list, safe=False)

  elif request.method == 'POST':
    try:
      body = request.body.decode() # Bytes.decode() -> String (Deserializtion)
      hero_name = json.loads(body)['name']
      hero_age = json.loads(body)['age']

    except (KeyError, JSONDecodeError) as e:
      return HttpResponseBadRequest(e)
    
    hero = Hero(name=hero_name, age=hero_age)
    hero.save()
    response_dict = { 'id': hero.id, 'name': hero.name }
    return JsonResponse(response_dict, status=201)
  
  else:
    return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id):
  if request.method == 'GET':
    hero = Hero.objects.get(pk=id)
    response_dict = { 'id': id, 'name': hero.name, 'age': hero.age}
    return JsonResponse(response_dict, status=200)
  
  elif request.method == 'PUT':
    hero = Hero.objects.get(pk=id)
    body = request.body.decode()
    hero.name = json.loads(body)['name']
    hero.age = json.loads(body)['age']
    hero.save()
    response_dict = { 'id': id, 'name': hero.name, 'age': hero.age}
    return JsonResponse(response_dict, status=204)
  
  else:
    return HttpResponseNotAllowed(['GET', 'PUT'])