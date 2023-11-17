from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from legosumodb.models import Competition as LegoSumoCompetition
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

            # Get the database connection and cursor
            connection = get_database_connection()
            cursor = connection.cursor()

            query = "SELECT Distinct Competition.Competition_id, Competition.name, Competition.games_per_team, Competition.date, Division_has_Competition.nbr_of_fields FROM Competition INNER JOIN Division_has_Competition ON Division_has_Competition.Competition_id = Competition.Competition_id;"
            
            cursor.execute(query)
            results = cursor.fetchall()

            data = [{'competition_id': result[0], 'name': result[1], 'games_per_team': result[2], 'date': result[3], 'nbr_of_fields': result[4]} for result in results]

            cursor.close()

            return JsonResponse({'competitions': data})
            

        except Exception as e:
            return JsonResponse({'error': 'An error occurred'}, status=500)


    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role','name', 'games_per_team', 'date', 'nbr_of_fields']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)

            access_role = data.get('access_role')
            name = data.get('name')
            games_per_team = data.get('games_per_team')
            nbr_of_fields = data.get('nbr_of_fields')

            try:
                date = datetime.strptime(data.get('date'), "%Y/%m/%d").date()
            
            except ValueError:
                return JsonResponse({'error': 'Invalid date format. Use "yyyy/mm/dd".'}, status=400)


            if (access_role == "Admin"):                


                new_competition, created = LegoSumoCompetition.objects.get_or_create(
                name=name, games_per_team=games_per_team, date=date
                )

                if created:
                    # Competition created successfully
                    response_data = {
                        'competition_id': new_competition.competition_id
                    }
                

                    division_ids = [1, 2, 3, 4]
                
                                
                    # Get the database connection and cursor
                    connection = get_database_connection()
                    
                    
                    for division_id in division_ids:
                        try:
                            cursor = connection.cursor()

                            query = "INSERT INTO Division_has_Competition (Division_id, Competition_id, nbr_of_fields) VALUES (%s,%s,%s)"
                            params = (division_id, new_competition.competition_id, nbr_of_fields)
                            
                            cursor.execute(query, params)

                            connection.commit()  # Commit the changes to the database
                            
#                            print(f"Inserted into Division_has_Competition: {params}")

                            cursor.close()

                        except Exception as e:
                            connection.rollback()  # Rollback changes in case of an error

                            return JsonResponse({'error': f'Error inserting records into Division_has_Competition: {str(e)}'}, status=500)
                        

                    return JsonResponse(response_data)
                
                else:
                    # Competition with the same attributes already exists
                    return JsonResponse({'error': 'Competition with the same attributes already exists'}, status=400)
                
                
            
            else:
                return JsonResponse({'error': 'You are not authorised to submit this request.'}, status=403)


        except IntegrityError as e:
            return JsonResponse({'error': 'A database integrity error occurred. Make sure the data is valid.'}, status=500)
        
        except ValueError as e:
            return JsonResponse({'error': 'Invalid date format. Use "yyyy/mm/dd".'}, status=400)
        
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

