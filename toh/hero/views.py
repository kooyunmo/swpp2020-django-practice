from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World!\n')


def hero_name(request, name=""):
    return HttpResponse('Your name is '+name+'\n')


def hero_id(request, id=3):
    return HttpResponse('Your id is '+str(id)+'\n')