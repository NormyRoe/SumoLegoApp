from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from legosumodb.models import Team as LegoSumoTeam
from legosumodb.models import School as LegoSumoSchool
from legosumodb.models import DivisionHasTeam as LegoSumoDivisionHasTeam
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

            query = "SELECT Division.name, Team.Team_id, Team.name, Team.School_id FROM Division_has_Team INNER JOIN Division ON Division.Division_id = Division_has_Team.Division_id INNER JOIN Team ON Division_has_Team.Team_id = Team.Team_id;;"
            
            cursor.execute(query)
            results = cursor.fetchall()

            data = [{'division_name': result[0], 'team_id': result[1], 'team_name': result[2], 'school_id': result[3]} for result in results]

            cursor.close()

            return JsonResponse({'teams': data})

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def RequestedSchool(request, ID):

    if request.method == 'GET':

        try:

            # Get the database connection and cursor
            connection = get_database_connection()
            cursor = connection.cursor()

            query = "SELECT Division.name, Team.Team_id, Team.name, Team.School_id FROM Division_has_Team INNER JOIN Division ON Division.Division_id = Division_has_Team.Division_id INNER JOIN Team ON Division_has_Team.Team_id = Team.Team_id WHERE Team.School_id = %s;"
            params = (ID,)

            cursor.execute(query, params)
            results = cursor.fetchall()

            data = [{'division_name': result[0], 'team_id': result[1], 'team_name': result[2]} for result in results]

            cursor.close()

            return JsonResponse({'teams': data})

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)


    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role','name', 'division_id']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)

            access_role = data.get('access_role')
            name = data.get('name')
            division_id = data.get('division_id')

            
            if (access_role == "Admin"):                


                school = LegoSumoSchool.objects.get(school_id=ID)

                new_team, created = LegoSumoTeam.objects.get_or_create(
                name=name, school=school
                )

                if created:
                    # Team created successfully
                    response_data = {
                        'team_id': new_team.team_id
                    }
                
                                
                    # Get the database connection and cursor
                    connection = get_database_connection()
                    
                    try:
                        cursor = connection.cursor()

                        query = "INSERT INTO Division_has_Team (Division_id, Team_id) VALUES (%s,%s)"
                        params = (division_id, new_team.team_id)
                            
                        cursor.execute(query, params)

                        connection.commit()  # Commit the changes to the database
                            
#                        print(f"Inserted into Division_has_Team: {params}")

                        cursor.close()

                    except Exception as e:
                        connection.rollback()  # Rollback changes in case of an error

                        return JsonResponse({'error': f'Error inserting records into Division_has_Team: {str(e)}'}, status=500)
                    
                    

                    return JsonResponse(response_data)
                
                else:
                    # Team with the same attributes already exists
                    return JsonResponse({'error': 'team with the same attributes already exists'}, status=400)
                
                
            
            else:
                return JsonResponse({'error': 'You are not authorised to submit this request.'}, status=403)


        except IntegrityError as e:
            return JsonResponse({'error': 'A database integrity error occurred. Make sure the data is valid.'}, status=500)


        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)



    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

   
@csrf_exempt
def RequestedTeam(request, ID):
    
    if request.method == 'PATCH':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role','name', 'division_id']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)

            access_role = data.get('access_role')
            name = data.get('name')
            division_id = data.get('division_id')

            
            if (access_role == "Admin"):                


                update_result = LegoSumoTeam.objects.filter(team_id=ID).update(name=name)

                # Check the value of update_result to determine if the update was successful.
                if update_result > 0:

                    # Team updated successfully

                    response_data = {
                        'message': 'Team update was successful.'
                    }

                    # Get the database connection and cursor
                    connection = get_database_connection()
                    
                    try:
                        cursor = connection.cursor()

                        query = "UPDATE Division_has_Team SET Division_id = %s WHERE Team_id = %s"
                        params = (division_id, ID)
                            
                        cursor.execute(query, params)

                        connection.commit()  # Commit the changes to the database
                            
                        print(f"Updated Division_has_Team: {params}")

                        cursor.close()

                    except Exception as e:
                        connection.rollback()  # Rollback changes in case of an error

                        return JsonResponse({'error': f'Error updating records into Division_has_Team: {str(e)}'}, status=500)


                    return JsonResponse(response_data)

                else:

                    # update_result is 0, which means no rows were updated.

                    response_data = {
                        'message': 'No changes were made. Team update was unsuccessful.'
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
