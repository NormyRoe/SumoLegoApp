from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from legosumodb.models import Competition as LegoSumoCompetition
from legosumodb.models import Division as LegoSumoDivision
from legosumodb.models import Team as LegoSumoTeam
from legosumodb.models import CheckedIn as LegoSumoCheckedIn
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import pymysql

from django.db import IntegrityError


# Create your views here.

@csrf_exempt
def TheModelView(request, ID):
    

    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role','division_id', 'team_id', 'checked_in']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)

            access_role = data.get('access_role')
            division_id = data.get('division_id')
            team_id = data.get('team_id')
            checked_in = data.get('checked_in')

            
            if (access_role == "Admin"):                

                competition = LegoSumoCompetition.objects.get(competition_id=ID)
                division = LegoSumoDivision.objects.get(division_id=division_id)
                team = LegoSumoTeam.objects.get(team_id=team_id)

                new_checkedin, created = LegoSumoCheckedIn.objects.get_or_create(
                competition_id=competition, division_id=division, team_id=team, checked_in=checked_in
                )

                if created:
                    # CheckedIn created successfully
                    response_data = {
                        'Checked_In_id': new_checkedin.checked_in_id
                    }
                

                    return JsonResponse(response_data)
                
                else:
                    # CheckedIn with the same attributes already exists
                    return JsonResponse({'error': 'Checked_In with the same attributes already exists'}, status=400)
                
                
            
            else:
                return JsonResponse({'error': 'You are not authorised to submit this request.'}, status=403)


        except IntegrityError as e:
            return JsonResponse({'error': 'A database integrity error occurred. Make sure the data is valid.'}, status=500)
        
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

