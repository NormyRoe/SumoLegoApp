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

    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role','first_name', 'surname', 'email_address', 
            'username', 'password', 'role']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)


            access_role = data.get('access_role')
            first_name = data.get('first_name')
            surname = data.get('surname')
            email_address = data.get('email_address')
            username = data.get('username')
            password = data.get('password')
            role = data.get('role')
            

            if (access_role == "Admin"):                


                new_user, created = LegoSumoUser.objects.get_or_create(
                first_name=first_name, surname=surname, email_address=email_address,
                username=username, password=password, role=role
                )

                if created:
                    # User created successfully

                    response_data = {
                        'user_id': new_user.user_id
                    }
                

                    return JsonResponse(response_data)
                
                else:
                    # User with the same attributes already exists
                    return JsonResponse({'error': 'User with the same attributes already exists'}, status=400)
                                
            
            else:
                return JsonResponse({'error': 'You are not authorised to submit this request.'}, status=403)


        except IntegrityError as e:
            return JsonResponse({'error': 'A database integrity error occurred. Make sure the data is valid.'}, status=500)
                
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)


    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def SpecificUser(request, ID):

    if request.method == 'PATCH':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role','first_name', 'surname', 'email_address', 
            'username', 'password']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)


            access_role = data.get('access_role')
            first_name = data.get('first_name')
            surname = data.get('surname')
            email_address = data.get('email_address')
            username = data.get('username')
            password = data.get('password')


            if (access_role == "Admin"):

                
                update_result = LegoSumoUser.objects.filter(user_id=ID).update(
                    first_name=first_name, surname=surname, email_address=email_address,
                username=username, password=password
                )

                # Check the value of update_result to determine if the update was successful.
                if update_result > 0:

                    # User updated successfully

                    response_data = {
                        'message': 'User update was successful.'
                    }

                    return JsonResponse(response_data)

                else:

                    # update_result is 0, which means no rows were updated.

                    response_data = {
                        'message': 'No changes were made. User update was unsuccessful.'
                    }
                    
                    return JsonResponse(response_data, status=400)
                                
            
            else:
                return JsonResponse({'error': 'You are not authorised to submit this request.'}, status=403)


        except IntegrityError as e:
            return JsonResponse({'error': 'A database integrity error occurred. Make sure the data is valid.'}, status=500)
                
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)


    if request.method == 'DELETE':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)


            access_role = data.get('access_role')


            if (access_role == "Admin"):

                
                delete_result = LegoSumoUser.objects.filter(user_id=ID).delete()

                # Check the value of delete_result to determine if the delete was successful.
                if delete_result[0] > 0:

                    # User deleted successfully

                    response_data = {
                        'message': 'User delete was successful.'
                    }

                    return JsonResponse(response_data)

                else:

                    # delete_result is 0, which means no rows were delete.

                    response_data = {
                        'message': 'No changes were made. User delete was unsuccessful.'
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

