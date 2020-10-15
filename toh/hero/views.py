from json import JSONDecodeError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero
from django.forms.models import model_to_dict


# Create your views here.
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
def hero_info(request, id=0):
    if request.method == 'GET':
        hero = Hero.objects.get(id=id)
        return JsonResponse(model_to_dict(hero), safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body).get('name')
            hero_age = json.loads(body).get('age')
            hero = Hero.objects.get(id=id)
            if hero_name:
                hero.name = hero_name
            if hero_age:
                hero.age = hero_age
            hero.save()
            return JsonResponse(model_to_dict(hero), status=201)
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])



def index(request):
    return HttpResponse("Hello, world!")

def showUrlNumber(request, number=0):
    return HttpResponse(f'Your number is {number}')

def showUrlText(request, text=""):
    return HttpResponse(f'Your given String is {text}')