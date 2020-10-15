from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world!")

def hero_id(request, id_=""):
	return HttpResponse(f"Your id is {id_}!")

def hero_name(request, name=""):
	return HttpResponse(f"Your name is {name}!")
