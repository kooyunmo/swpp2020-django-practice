# TODO: controller 부분. url에 해당하는 알맞는 view function
from json import JSONDecodeError
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero


# Create your views here.

def index(request):
    return HttpResponse("Hello world.")


def hero_name(request, name):
    return HttpResponse(f'your name is {name}')


#    return HttpResponse('your name is ', name)
@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)  # serailization
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
        return HttpResponseNotAllowed(['GET', 'POST'])  # 이거 이외에는 허용되지 않는 request다.


@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.filter(id=id).values()]
        return JsonResponse(hero_all_list, safe=False)  # serailization
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        selected_hero = Hero.objects.get(id=id)
        selected_hero.name = hero_name
        selected_hero.age = hero_age
        selected_hero.save()
        response_dict = {'id': selected_hero.id, 'name': selected_hero.name, 'age': selected_hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])
