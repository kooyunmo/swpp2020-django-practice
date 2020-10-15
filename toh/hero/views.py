import json
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import JSONDecodeError
from .models import Hero


@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            name = json.loads(body)['name']
            age = json.loads(body)['age']
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()
        hero = Hero(name=name, age=age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'score': hero.score}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def hero_info(request, id=0):
    if request.method == 'GET':
        found_hero = Hero.objects.filter(id=id).first()
        response_dict = {
            'name': found_hero.name, 'age': found_hero.age}
        return JsonResponse(response_dict, safe=False)
    elif request.method == 'PUT':
        print('PUT')
        try:
            body = request.body.decode()
            name = json.loads(body)['name']
            age = json.loads(body)['age']
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()
        hero = Hero.objects.filter(id=id).first()
        hero.name = name
        hero.age = age
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])


def index(request):
    return HttpResponse('Hello, world!')


def hero_name(request, name=""):
    return HttpResponse('Your name is ' + name + '!')


def hero_id(request, id=0):
    return HttpResponse('Your id is ' + str(id) + '!')
