from django.shortcuts import render
from django.http import HttpResponse,\
    HttpResponseBadRequest,\
    HttpResponseNotAllowed,\
    JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero

# Create your views here.
def index(request):
    return HttpResponse('hello hero')

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            body_dict = json.loads(body)
            hero_name = body_dict['name']
            hero_age = body_dict['age']
        except (KeyError, json.JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = { 'id': hero.id, 'name': hero.name, 'age': hero.age };
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id):
    target = Hero.objects.filter(id=id)
    if not target.exists():
        return HttpResponseBadRequest()

    if request.method == 'GET':
        return JsonResponse(target.values()[0], safe=False)
    elif request.method == 'PUT':
        my_hero = target[0]
        try:
            body = request.body.decode()
            body_dict = json.loads(body)
            hero_name = body_dict.get('name', my_hero.name)
            hero_age = body_dict.get('age', my_hero.age)
        except (KeyError, json.JSONDecodeError) as e:
            return HttpResponseBadRequest()
        my_hero.name = hero_name
        my_hero.age = hero_age
        my_hero.save()
        response_dict = {
            'id': my_hero.id,
            'name': my_hero.name,
            'age': my_hero.age
        };
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])
