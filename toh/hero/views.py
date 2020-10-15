from django.http import HttpResponse

def index(request):
  return HttpResponse('Hello, world!')

def hero_name(request, name=''):
  return HttpResponse("Your name is {}!".format(name))

def hero_id(request, id=-1):
  return HttpResponse("Your id is {}!".format(id))
# Create your views here.

from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero, Team
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
def hero_info(request, id=-1):
    if request.method == 'GET':
        # hero_all_list = [hero for hero in Hero.objects.all().values()]
        hero_obj = Hero.objects.filter(id=id)[0]
        response_dict = {'id': hero_obj.id, 'name': hero_obj.name, 'age': hero_obj.age}  
        return JsonResponse(response_dict, safe=False)
    elif request.method == 'PUT': 
        hero_obj = Hero.objects.filter(id=id)[0]
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age'] 
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        # hero = Hero(name=hero_name, age=hero_age)

        hero_obj.name = hero_name
        hero_obj.age = hero_age
        hero_obj.save()
        response_dict = {'id': hero_obj.id, 'name': hero_obj.name, 'age': hero_obj.age} 
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])