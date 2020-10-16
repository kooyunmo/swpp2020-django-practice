from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json 
from .models import * 

def index(request):
  return HttpResponse('Hello, world!')

def hero_id(request, id):
  print('Your id is ', id)
  return HttpResponse("Your id is " + str(id) + "!")

def hero_name(request, name=""):
  print('Your name is ', name)
  return HttpResponse('Your name is ' + name + "!")

@csrf_exempt
def hero_info(request, id):
  if request.method == 'GET':
    hero = [hero for hero in Hero.objects.all().values() if hero['id'] == id]
    return JsonResponse(hero, safe=False)
  elif request.method == 'PUT':
    try: 
      body = request.body.decode()
      hero_name = json.loads(body)['name']
      hero_age = json.loads(body)['age']

    except(KeyError, JSONDecodeError) as e: 
      return HttpResponseBadRequest()
    
    hero = Hero.objects.all().get(id=id)
    hero.name = hero_name
    hero.age = hero_age
    hero.save()
    response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
    return JsonResponse(response_dict, statue=201)

@csrf_exempt
def hero_list(request):
  if request.method == 'GET':
    hero_all_list = [hero for hero in Hero.objects.all().values()]
    return JsonResponse(hero_all_list, safe=False)
  # serialization을 위해서 safe=False를 사용해야한다. 
  elif request.method == 'POST':
    try: 
      body = request.body.decode()
      hero_name = json.loads(body)['name'] 

    except(KeyError, JSONDecodeError) as e:
      return HttpResponseBadRequest()
    
    hero = Hero(name=hero_name)
    hero.save()
    response_dict = {'id': hero.id, 'name': hero.name} 
    return JsonResponse(response_dict, status=201)

  else:
    return HttpResponseNotAllowed(['GET', 'POST'])
