from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
import json
from .models import Hero
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')

def hero_name(request, name):
    return HttpResponse('Your name is {}!'.format(name))

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

@csrf_exempt
def hero_info(request, req_id):
    if request.method == 'GET':
        match_hero = Hero.objects.get(id=req_id)
        # return JsonResponse(list(match_hero.values())[0])
        # return JsonResponse({'id': match_hero.id, 'name': match_hero.name, 'age': match_hero.age})
        return JsonResponse({'id': 1, 'name': 'aa', 'age': 11})
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_new_name = json.loads(body)['name']
            hero_new_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        match_hero = Hero.objects.get(id=req_id)
        match_hero.name = hero_new_name
        match_hero.age = hero_new_age
        match_hero.save()
        response_dict = {'id' : match_hero.id, 'name' : match_hero.name, 'age': match_hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])