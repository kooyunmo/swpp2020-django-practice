from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
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
		except (KeyError, JSONDecodeError) as e:
			return HttpResponseBadRequest()
		hero = Hero(name=hero_name)
		hero.save()
		response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
		return JsonResponse(response_dict, status=201)
	else:
		return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_view(request, id_=0):
	if request.method == 'GET':
		q = Hero.objects.filter(id=id_)
		if not q.exists():
			return HttpResponseNotFound()

		obj = q.get()
		return JsonResponse({
			'id': obj.id,
			'name': obj.name,
			'age': obj.age,
		}, safe=False, status=200)

	if request.method == 'PUT':
		try:
			body = request.body.decode()
			qobj = json.loads(body)
		except (KeyError, JSONDecodeError) as e:
			return HttpResponseBadRequest()

		obj = Hero(id=id_, name=qobj['name'], age=qobj['age'])
		obj.save()
		return JsonResponse({'id': obj.id, 'name': obj.name, 'age': obj.age}, status=200)

	return HttpResponseNotAllowed(['GET', 'PUT'])
