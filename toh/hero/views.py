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
        hero = Hero(name = hero_name, age = hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, target_id):
    if request.method == 'GET':

        target_hero = Hero.objects.get(id=target_id)
        response_dict = {'id': target_hero.id, 'name': target_hero.name, 'age': target_hero.age}

        return JsonResponse(response_dict, status=201)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            change_name = json.loads(body)['name']
            change_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        
        target_hero = Hero.objects.get(id=target_id)
        target_hero.name = change_name
        target_hero.age = change_age
        target_hero.save()
        response_dict = {'id': target_hero.id, 'name': target_hero.name, 'age': target_hero.age}

        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET','PUT'])





#### prac 1
#def index(request):
#    return HttpResponse('Hello, world!')
#
#def hero_id(request, id):
#    return HttpResponse(f'Your ID is {id}')
#
#def hero_name(request, name):
#    return HttpResponse(f'Your name is {name}')
