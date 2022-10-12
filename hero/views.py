from django.shortcuts import render
from django.http import HttpRequest, HttpResponseBadRequest,HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
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
          response_dict = {'id': hero.id, 'name': hero.name}
          return JsonResponse(response_dict, status=201)
    else:
          return HttpResponseNotAllowed(['GET', 'POST'])
@csrf_exempt
def hero_info(request ,id=0):
    if request.method == 'GET':
          hero_to_get = list(Hero.objects.all().filter(pk=str(id)).values())
          return JsonResponse(hero_to_get, safe=False)
    elif request.method == 'PUT':
        try:
                body = request.body.decode()
                hero_name = json.loads(body)['name']
                hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
                return HttpResponseBadRequest()
        hero = Hero.objects.all().get(pk=str(id))
        hero.name=hero_name
        hero.age=hero_age
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name ,'age':hero.age}
        return JsonResponse(response_dict, status=300)
    else:
          return HttpResponseNotAllowed(['GET', 'PUT'])

def hero_id(request ,id=0):
    return HttpResponse('Your id is '+ str(id))
def hero_name(request ,name=""):
    return HttpResponse('Your name is '+ name)    
