from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from legosumodb.models import Field as LegoSumoField
from legosumodb.models import Division as LegoSumoDivision
from legosumodb.models import Team as LegoSumoTeam
from legosumodb.models import GameResult as LegoSumoGameResult
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import pymysql

from django.db import IntegrityError


# Create your views here.

@csrf_exempt
def TheModelView(request, ID):
    

    if request.method == 'GET':

        try:
            
            gameresults = LegoSumoGameResult.objects.filter(competition_id=ID)

            # Convert database results into a list of dictionaries
            data = []
            for gameresult in gameresults:
                data.append({
                    'game_id': gameresult.game_id,
                    'division': gameresult.division.name,
                    'round': gameresult.round,
                    'field': gameresult.field.name,
                    'start_time': gameresult.start_time,
                    'team1': gameresult.team1.name,
                    'team1_points': gameresult.team1_points,
                    'team2': gameresult.team2.name,
                    'team2_points': gameresult.team2_points
                })

            return JsonResponse({'Game_Results': data})
       

        except Exception as e:
            import logging
            logging.error(str(e))  # Log the exception
            return JsonResponse({'error': 'An error occurred'}, status=500)


    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def SubmitScore(request, ID):
    
    
    if request.method == 'PATCH':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role','team1_points', 'team2_points']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)

            access_role = data.get('access_role')
            team1_points = data.get('team1_points')
            team2_points = data.get('team2_points')

            
            if (access_role == "Judge"):                


                update_result = LegoSumoGameResult.objects.filter(game_id=ID).update(team1_points=team1_points, team2_points=team2_points)

                # Check the value of update_result to determine if the update was successful.
                if update_result > 0:

                    # Game_Result updated successfully

                    response_data = {
                        'message': 'Game_Result update was successful.'
                    }

                    
                    return JsonResponse(response_data)

                else:

                    # update_result is 0, which means no rows were updated.

                    response_data = {
                        'message': 'No changes were made. Game_Result update was unsuccessful.'
                    }

                    
                    return JsonResponse(response_data, status=400)
                
            
            else:
                return JsonResponse({'error': 'You are not authorised to submit this request.'}, status=403)


        except IntegrityError as e:
            return JsonResponse({'error': 'A database integrity error occurred. Make sure the data is valid.'}, status=500)


        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)


    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


