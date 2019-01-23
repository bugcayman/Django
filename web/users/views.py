from django.shortcuts import render,reverse,redirect
import json
from django.http import HttpResponse,HttpResponseBadRequest,JsonResponse
# Create your views here.
from django.http import HttpResponse
def index(request):
    """index视图"""
    return HttpResponse("HELLO THE WORLD")


def redirect_demo(request):

    print(reverse(index))

    return HttpResponse('redirect_demo')

def reverse_demo(request):
    print(reverse('namespace:index'))
    return HttpResponse('23')

def weather(request,city,year):
    print('city=%s'%city)
    print('year=%s'%year)
    return HttpResponse('OK')
