from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from legosumodb.models import User as LegoSumoUser
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import pymysql

from django.db import IntegrityError


# Create your views here.

@csrf_exempt
def TheModelView(request):

    if request.method == 'GET':

        try:
            
            users = LegoSumoUser.objects.all()

            # Convert database results into a list of dictionaries
            data = [{'user_id': user.user_id,'first_name': user.first_name,
            'surname': user.surname, 'email_address': user.email_address,
            'username': user.username, 'role': user.role} for user in users]

            return JsonResponse({'users': data})
       

        except Exception as e:
            return JsonResponse({'error': 'An error occurred'}, status=500)


    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

