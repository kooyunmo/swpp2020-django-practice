from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import *
from .models import *
import json
def index(request):
	return HttpResponse("Hello World!")

@csrf_exempt
def hero_info(request, _id : int):
	if request.method == 'GET':
		try:
			hero = Hero.objects.filter(id=_id).all().values()[0]
			respose_dict = {'id': hero['id'], 'name':hero['name'], 'age':hero['age']}
			return JsonResponse(respose_dict, status=201)
		except (KeyError, ValueError) as e:
			return HttpResponseBadRequest()
	elif request.method == 'PUT':
		print(f"PUT TRY")
		try:
			body = request.body.decode()
			j = json.loads(body)
			hero_name, hero_age = j['name'], j['age']
			Hero.objects.filter(id=_id).update(name=hero_name, age=hero_age)
			respose_dict = {
				'id': _id,
				'name':hero_name,
				'age':hero_age
			}
			return JsonResponse(respose_dict, status=201)
		except (KeyError, ValueError) as e:
			return HttpResponseBadRequest()
	else:
		return HttpResponseNotAllowed(['GET', 'PUT'])

def NAME(request, _name : str):
	return HttpResponse(f"Hello my Name is {_name}")

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
		except (KeyError, ValueError) as e:
			return HttpResponseBadRequest()
		hero = Hero(name=hero_name, age=hero_age)
		hero.save()
		respose_dict = {'id': hero.id, 'name':hero.name, 'age':hero.age}
		return JsonResponse(respose_dict, status=201)
	else:
		return HttpResponseNotAllowed(['GET', 'POST'])