from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from legosumodb.models import Division as LegoSumoDivision
from legosumodb.models import DivisionHasCompetition as LegoSumoDivisionHasCompetition
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import pymysql
from .database_utils import get_database_connection
from django.db import IntegrityError


# Create your views here.

@csrf_exempt
def TheModelView(request):

    if request.method == 'GET':

        try:
            
            divisions = LegoSumoDivision.objects.all()

            # Convert database results into a list of dictionaries
            data = [{'division_id': division.division_id,'name': division.name} for division in divisions]

            return JsonResponse({'divisions': data})
       

        except Exception as e:
            return JsonResponse({'error': 'An error occurred'}, status=500)


    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def RequestedCompetition(request, ID):

    if request.method == 'GET':

        try:

            # Get the database connection and cursor
            connection = get_database_connection()
            cursor = connection.cursor()

            query = "SELECT Division.Division_id, Division.name FROM Division_has_Competition INNER JOIN Division ON Division_has_Competition.Division_id = Division.Division_id WHERE Division_has_Competition.Competition_id = %s;"
            params = (ID,)

            cursor.execute(query, params)
            results = cursor.fetchall()

            data = [{'division_id': result[0], 'name': result[1]} for result in results]

            cursor.close()

            return JsonResponse({'divisions': data})

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)


    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

   