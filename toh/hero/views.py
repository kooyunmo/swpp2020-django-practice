from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Hero

# Create your views here.
def index(request):
	return HttpResponse('Hello, world!')

def hero_name(request, name=""):
	return HttpResponse('Your name is ' + name + "!")

def hero_id(request, id=""):
	return HttpResponse('Your id is ' + id + "!")

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
			hero_score = json.loads(body)['score']
		except (KeyError, JSONDecodeError) as e:
			return HttpResponseBadRequest()
		hero = Hero(name=hero_name, age=hero_age)
		hero.save()
		response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age, 'score': hero.score}
		return JsonResponse(response_dict, status=201)
	else:
		return HttpResponseNotAllowed(['GET', 'POSET'])

@csrf_exempt
def hero_info(request, id=""):
	if request.method == 'GET':
		hero = Hero.objects.get(id=id)
		response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age, 'score': hero.score}
		return JsonResponse(response_dict, status=500)
	elif request.method == 'PUT':
		try:
			body = request.body.decode()
			hero_name = json.loads(body)['name']
			hero_age = json.loads(body)['age']
			hero_score = json.loads(body)['score']
		except (KeyError, JSONDecodeError) as e:
			return HttpResponseBadRequest()
		hero = Hero.objects.get(id=id)
		hero.name = hero_name
		hero.age = hero_age
		hero.score = hero_score
		hero.save()
		response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age, 'score': hero.score}
		return JsonResponse(response_dict, status=200)
	else:
		return HttpResponseNotAllowed(['GET'])
