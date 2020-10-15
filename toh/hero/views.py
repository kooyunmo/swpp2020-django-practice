from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('Hello, world!')

def hero_id(request, id=0):
  return HttpResponse('Your id is ' + str(id) + '!')

def hero_name(request, name=""):
  return HttpResponse('Your name is ' + name + '!')
