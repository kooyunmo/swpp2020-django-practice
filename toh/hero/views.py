from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero

# Create your views here.
@csrf_exempt
def hero_id(request, id):
    return HttpResponse('Your id is ' + str(id))

@csrf_exempt
def hero_name(request, name):
    return HttpResponse('Your name is ' + name)

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name=json.loads(body)['name']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id':hero.id, 'name':hero.name, 'age':hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

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


