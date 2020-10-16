from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero

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
        response_dict = {'id': hero.id, 'name': hero.name, 'age':hero.age}
        return JsonResponse(response_dict,status=201)
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@csrf_exempt
def hero_info(request, id=1):
    if request.method == 'GET':
        try:
            hero_found = Hero.objects.get(id=id)
            # print('here') # this is printed on the server side terminal
        except (DoesNotExist, MultipleObjectsReturned) as e:
            return HttpResponseBadRequest()
        response_dict = {'id': hero_found.id, 'name': hero_found.name, 'age':hero_found.age}
        return JsonResponse(response_dict,status=201)
    elif request.method == 'PUT':
        try:
            hero_found = Hero.objects.get(id=id)
        except (DoesNotExist, MultipleObjectsReturned) as e:
            return HttpResponseBadRequest()

        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        
        hero_found.name= hero_name
        hero_found.age = hero_age
        hero_found.save()
        response_dict= {'id': hero_found.id, 'name': hero_found.name, 'age':hero_found.age}
        return JsonResponse(response_dict,status=201)
    else:
        return HttpResponseNotAllowed(['GET','PUT'])
    