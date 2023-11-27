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
                division_name = gameresult.division.name if gameresult.division else 'None'
                team1_name = gameresult.team1.name if gameresult.team1 else 'None'
                team2_name = gameresult.team2.name if gameresult.team2 else 'None'
                team1_school_name = gameresult.team1.school.name if gameresult.team1 and gameresult.team1.school else 'None'
                team2_school_name = gameresult.team2.school.name if gameresult.team2 and gameresult.team2.school else 'None'
                

                data.append({
                    'game_id': gameresult.game_id,
                    'division': division_name,
                    'round': gameresult.round,
                    'field': gameresult.field.name if gameresult.field else 'None',
                    'start_time': gameresult.start_time,
                    'team1': team1_name,
                    'team1_points': gameresult.team1_points,
                    'team1_school': team1_school_name,
                    'team2': team2_name,
                    'team2_points': gameresult.team2_points if gameresult.team2_points else '0',
                    'team2_school': team2_school_name
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


