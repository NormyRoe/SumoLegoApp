from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from legosumodb.models import User as LegoSumoUser
from django.views.decorators.csrf import csrf_exempt
import json
import pymysql


# Create your views here.

def TheModelView(request):

    if request.method == 'GET':

        try:

            #query parameters
            username = request.GET.get('username')
            password = request.GET.get('password')

            if username and password:
                
                try:
                    
                    user = LegoSumoUser.objects.get(username=username, password=password)
                    response_data = {
                        'role': user.role
                    }

                    return JsonResponse(response_data)
                
                except LegoSumoUser.DoesNotExist:
                    return JsonResponse({'error': 'User not found'}, status=404)

            else:
                return JsonResponse({'error': 'Invalid query parameters'}, status=500)

        except Exception as e:
            return JsonResponse({'error': 'An error occurred'}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

