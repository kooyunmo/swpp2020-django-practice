from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero

# Create your views here.
def index(request):
    return HttpResponse('Hello world')

def hero_name(request, name=""):
    return HttpResponse('Your name is '+ name)

def hero_id(request, id=""):
    return HttpResponse('Your id is {}'.format(id))

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
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name} 
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id_search=""):
    if request.method == 'GET':
        h = Hero.objects.filter(id=id_search).values()
        hero_found = [hero for hero in h]
        return JsonResponse(hero_found, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_modified_name = json.loads(body)['name']
            hero_modified_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero.objects.get(id=id_search)
        hero.name = hero_modified_name
        hero.age = hero_modified_age
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
