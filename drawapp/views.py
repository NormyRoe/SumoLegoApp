from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
from django.utils import timezone
from legosumodb.models import Competition

from drawapp.utils import GenerateRoundsForCompetition, GetCompetitionForCompetitionId

import json


@csrf_exempt
def CreateDrawForCompetition(request, competition_id):
    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            required_fields = ['access_role']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)

            access_role = data.get('access_role')
            
            
            if (access_role == "Admin"):

                try:
                    competition = GetCompetitionForCompetitionId(competition_id)
                    GenerateRoundsForCompetition(
                        competition_id=competition_id,
                        startTime=timezone.now() + timedelta(minutes=10)
                    )
                    
                    return JsonResponse({"messsage": "Completed generation of rounds"}, status=200)

                except Competition.DoesNotExist as e:
                    return JsonResponse({"messsage": f"Competition with ID {competition_id} not found"}, status=404)

                except Exception as e:
                    return JsonResponse({"messsage": "Could not generate rounds"}, status=500)
                
            
            else:
                return JsonResponse({'error': 'You are not authorised to submit this request.'}, status=403)


        except IntegrityError as e:
            return JsonResponse({'error': 'A database integrity error occurred. Make sure the data is valid.'}, status=500)
        
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

        
        
    else:
        return HttpResponse(status=405)
