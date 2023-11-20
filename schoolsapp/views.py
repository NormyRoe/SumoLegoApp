from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from legosumodb.models import School as LegoSumoSchool
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
            
            schools = LegoSumoSchool.objects.all()

            # Convert database results into a list of dictionaries
            data = [{'school_id': school.school_id,'name': school.name,
             'street_address_line_1': school.street_address_line_1,
             'street_address_line_2': school.street_address_line_2,
             'suburb': school.suburb, 'state': school.state, 'postcode': school.postcode,
             'contact_name': school.contact_name, 'contact_number': school.contact_number,
             'email_address': school.email_address, 'paid': school.paid} for school in schools]

            return JsonResponse({'schools': data})
       

        except Exception as e:
            return JsonResponse({'error': 'An error occurred'}, status=500)


    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role','name', 'street_address_line_1', 'street_address_line_2', 
            'suburb', 'state', 'postcode', 'contact_name', 'contact_number', 'email_address', 'paid']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)


            access_role = data.get('access_role')
            name = data.get('name')
            street_address_line_1 = data.get('street_address_line_1')
            street_address_line_2 = data.get('street_address_line_2')
            suburb = data.get('suburb')
            state = data.get('state')
            postcode = data.get('postcode')
            contact_name = data.get('contact_name')
            contact_number = data.get('contact_number')
            email_address = data.get('email_address')
            paid = data.get('paid')



            if (access_role == "Admin"):                


                new_school, created = LegoSumoSchool.objects.get_or_create(
                name=name, street_address_line_1=street_address_line_1, street_address_line_2=street_address_line_2,
                suburb=suburb, state=state, postcode=postcode, contact_name=contact_name, contact_number=contact_number,
                email_address=email_address, paid=paid
                )

                if created:
                    # School created successfully

                    response_data = {
                        'school_id': new_school.school_id
                    }
                

                    return JsonResponse(response_data)
                
                else:
                    # Competition with the same attributes already exists
                    return JsonResponse({'error': 'School with the same attributes already exists'}, status=400)
                                
            
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


@csrf_exempt
def UpdateSchool(request, ID):

    if request.method == 'PATCH':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role','name', 'street_address_line_1', 'street_address_line_2', 
            'suburb', 'state', 'postcode', 'contact_name', 'contact_number', 'email_address', 'paid']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)


            access_role = data.get('access_role')
            name = data.get('name')
            street_address_line_1 = data.get('street_address_line_1')
            street_address_line_2 = data.get('street_address_line_2')
            suburb = data.get('suburb')
            state = data.get('state')
            postcode = data.get('postcode')
            contact_name = data.get('contact_name')
            contact_number = data.get('contact_number')
            email_address = data.get('email_address')
            paid = data.get('paid')



            if (access_role == "Admin"):                


                # Instead of using "update_school, updated =", use a single variable for the update result.
                update_result = LegoSumoSchool.objects.filter(school_id=ID).update(
                    name=name, street_address_line_1=street_address_line_1, street_address_line_2=street_address_line_2,
                    suburb=suburb, state=state, postcode=postcode, contact_name=contact_name, contact_number=contact_number,
                    email_address=email_address, paid=paid
                )

                # Check the value of update_result to determine if the update was successful.
                if update_result > 0:

                    # School updated successfully

                    response_data = {
                        'message': 'School update was successful.'
                    }

                    return JsonResponse(response_data)

                else:

                    # update_result is 0, which means no rows were updated.

                    response_data = {
                        'message': 'No changes were made. School update was unsuccessful.'
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

