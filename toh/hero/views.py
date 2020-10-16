from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero 

def index(request):
    return HttpResponse('시발아')

def hero_id(request, id=0):
    return HttpResponse('Your id is {}'.format(id))

def hero_name(request, name=''):
    return HttpResponse('Your name is {}'.format(name))

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
        hero = Hero(name=hero_name, age = hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST']) 
        
@csrf_exempt 
def hero_info(request, id=0):
    if request.method == 'GET':
        taget_hero = [hero for hero in Hero.objects.filter(id=id).values()]
        return JsonResponse(taget_hero[0], safe=False)
    
    elif request.method == 'PUT':
        hero = Hero.objects.get(id=id)
        try:
            
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=200)

    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])

