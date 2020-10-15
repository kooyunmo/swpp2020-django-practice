from django.http import HttpResponse,  HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json import JSONDecodeError
from .models import Hero
@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list=[hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method =='POST':
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
def hero_info(request, targetid):
    if request.method == 'GET':
        hero = Hero.objects.get(id=targetid)
        response_dict ={'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, safe=True)
    elif request.method =='PUT':
         body = request.body.decode()
         hero_name = json.loads(body)['name']
         hero_age = json.loads(body)['age']
         hero=Hero.objects.get(id=targetid)
         hero.name=hero_name
         hero.age=hero_age
         hero.save()
         return JsonResponse({'id': hero.id, 'name': hero.name, 'age': hero_age}, safe=True)
def heroname(request, name=""):
    return HttpResponse(f'Your name is { name }') 
def heroid(request, id=0):
    return HttpResponse(f'Your id is { id }')
# Create your views here.
