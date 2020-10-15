from django.http import HttpResponse

def index(request):
  return HttpResponse('Hello, world!')

def hero_name(request, name=''):
  return HttpResponse("Your name is {}!".format(name))

def hero_id(request, id=-1):
  return HttpResponse("Your id is {}!".format(id))
# Create your views here.
