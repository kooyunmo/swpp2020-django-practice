from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from json import JSONDecodeError

import json 
from .models import Hero 

# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')

def hero_id(request, id=0):
    return HttpResponse("Your id is " + str(id) + "!")

def hero_name(request, name=""):
    return HttpResponse("Your name is " + name + "!")

@csrf_exempt 
def hero_list(request): 
    if request.method == 'GET': # Returning whole hero set
        hero_all_list = [hero for hero in Hero.objects.all().values()] 
        return JsonResponse(hero_all_list, safe=False) # safe=False : can be passed for serialization

    elif request.method == 'POST': 
        try: 
            body = request.body.decode() 
            hero_name = json.loads(body)['name'] 
        except (KeyError, JSONDecodeError) as e: 
            return HttpResponseBadRequest() 
        hero = Hero(name=hero_name, age=hero_age) 
        hero.save() 
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age} 
        return JsonResponse(response_dict) 

    else: 
        return HttpResponseNotAllowed(['GET', 'POST']) 

@csrf_exempt 
def hero_info(request, id): # regarding the URL

    if request.method == 'GET':
        hero_selected = [hero for hero in Hero.objects.filter(id=id).values()] 
        return JsonResponse(hero_selected, safe=False) 

    elif request.method == 'PUT':
        try: 
            body = request.body.decode() 
            hero_new_name = json.loads(body)['name']
            hero_new_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e: 
            return HttpResponseBadRequest()
        hero_selected = Hero.objects.get(id=id)
        hero_selected.name = hero_new_name
        hero_selected.age = hero_new_age
        hero_selected.save() # To save the modified data
        response_dict = {'id': hero_selected.id, 'name': hero_selected.name, 'age': hero_selected.age} 
        return JsonResponse(response_dict, status=201) 

    else :
        return HttpResponseNotAllowed(['GET', 'PUT']) 
