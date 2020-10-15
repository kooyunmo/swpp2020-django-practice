from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero
from json import JSONDecodeError

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

        hero = Hero(name=hero_name,age= hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name,'age':hero.age} 

        return JsonResponse(response_dict, status=201)

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request,id=0):
    if request.method == 'GET':
        hero = Hero.objects.get(id=id)
        jhero = {'id': hero.id, 'name':hero.name,'age':hero.age}
        return JsonResponse(jhero)

    elif request.method =='PUT':
        try:
            body = request.body.decode()
            new_hero_name = json.loads(body)['name']
            new_hero_age = json.loads(body)['age']
        except(KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()

        hero = Hero.objects.get(id=id)
        hero.name = new_hero_name
        hero.age = new_hero_age
        hero.save()

        response_dict ={'id': hero.id, 'name':hero.name, 'age': hero.age}
        return JsonResponse(response_dict,status=200)

    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])