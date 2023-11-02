from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from legosumodb.models import Field as LegoSumoField
from legosumodb.models import DivisionHasField as LegoSumoDivisionHasField
from legosumodb.models import User as LegoSumoUser
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

            query = "SELECT Field.Field_id, Field.name as 'Field_Name', User.username, Division.name AS 'Division_Name' FROM Field INNER JOIN User ON Field.judge = User.User_id INNER JOIN Division_has_Field ON Field.Field_id = Division_has_Field.Field_id INNER JOIN Division ON Division_has_Field.Division_id = Division.Division_id;"
            
            cursor.execute(query)
            results = cursor.fetchall()

            data = [{'field_id': result[0], 'name': result[1], 'division': result[3], 'judge': result[2]} for result in results]

            cursor.close()

            return JsonResponse({'fields': data})

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)


    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role','name', 'division_id', 'password', 'role']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)

            access_role = data.get('access_role')
            name = data.get('name')
            division_id = data.get('division_id')
            password = data.get('password')
            role = data.get('role')

            if (access_role == "Admin"):                


                new_user, created = LegoSumoUser.objects.get_or_create(
                username=name, password=password, role=role
                )

                if created:
                    # User created successfully

                    new_field, created = LegoSumoField.objects.get_or_create(
                name=name, judge=new_user
                )

                    if created:
                        # Field created successfully

                        response_data = {
                            'field_id': new_field.field_id
                        }
                            
                                    
                        # Get the database connection and cursor
                        connection = get_database_connection()
                        
                        try:
                            cursor = connection.cursor()

                            query = "INSERT INTO Division_has_Field (Division_id, Field_id) VALUES (%s,%s)"
                            params = (division_id, new_field.field_id)
                                
                            cursor.execute(query, params)

                            connection.commit()  # Commit the changes to the database
                                
#                            print(f"Inserted into Division_has_Field: {params}")

                            cursor.close()

                        except Exception as e:
                            connection.rollback()  # Rollback changes in case of an error

                            return JsonResponse({'error': f'Error inserting records into Division_has_Field: {str(e)}'}, status=500)
                        
                        
                        return JsonResponse(response_data)
                    
                    else:
                        # Competition with the same attributes already exists
                        return JsonResponse({'error': 'Field with the same attributes already exists'}, status=400)

                else:
                    # Competition with the same attributes already exists
                    return JsonResponse({'error': 'User with the same attributes already exists'}, status=400)

            
            else:
                return JsonResponse({'error': 'You are not authorised to submit this request.'}, status=403)



        except IntegrityError as e:
            return JsonResponse({'error': 'A database integrity error occurred. Make sure the data is valid.'}, status=500)
          
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)


    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    



