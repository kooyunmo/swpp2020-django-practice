# from django.http import HttpResponse
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero
from django.forms.models import model_to_dict

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
def hero_info(request, id=1):
    if request.method == 'GET':
        selectedHero = Hero.objects.get(id=id)
        return JsonResponse(model_to_dict(selectedHero), safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero = Hero.objects.get(id=id)
            name = json.loads(body).get('name')
            age = json.loads(body).get('age')
            if name:
                hero.name = name
            if age:
                hero.age = age
            hero.save()
            return JsonResponse(model_to_dict(hero), status=201)
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()    
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])


def index(request):
    return HttpResponse('Hello, world!')

def id(request, id=1):
    return HttpResponse('Your id is ' + str(id)+ '!')

def hero_name(request, name="aaa"):
    return HttpResponse('Your name is '+ name +'!')


