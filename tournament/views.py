from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Team
from django.http import JsonResponse
import json
# Create your views here.
@csrf_exempt
def list_teams(request):
    if request.method == 'GET':
        if "country" in request.GET:
            teams = Team.objects.filter(country=request.GET["country"])
        else:
            teams = Team.objects.all()
        return JsonResponse(serializers.serialize(queryset=teams, format='json'), safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        # new_team = Team(name=data['name'], description=data['description'], country=data['country'], logo=data['logo'])
        # new_team.save()
        new_team = Team.objects.create(**data)
        return JsonResponse(serializers.serialize(queryset=[new_team], format='json'), safe=False)
    
    if request.method == 'DELETE':
        data = json.loads(request.body)
        #team = Team.objects.get(id=data['id'])
        team = Team.objects.get(pk=data['id'])
        team.delete()
        return HttpResponse(status=204)

    if request.method == 'PUT':
        data = json.loads(request.body)
        #team = Team.objects.get(id=data['id'])
        team = Team.objects.get(pk=data['id'])
        team.name = data['name']
        team.save()
        return JsonResponse(serializers.serialize(queryset=[team], format='json'), safe=False)

    # print(request.body, "Esto es texto que me llega")
    # body  = json.loads(request.body.decode('utf-8'))
    # print(body, "Esto es texto en dict")
    # return HttpResponse("List of teams")