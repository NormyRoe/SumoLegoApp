from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
from django.utils import timezone
from legosumodb.models import Competition

from drawapp.utils import GenerateRoundsForCompetition, GetCompetitionForCompetitionId


@csrf_exempt
def CreateDrawForCompetition(request, competition_id):
    if request.method == 'POST':
        try:
            competition = GetCompetitionForCompetitionId(competition_id)
            GenerateRoundsForCompetition(
                competition=competition,
                startTime=timezone.now() + timedelta(minutes=10)
            )
            
            return JsonResponse({"messsage": "Completed generation of rounds"}, status=200)
        except Competition.DoesNotExist as e:
            return JsonResponse({"messsage": f"Competition with ID {competition_id} not found"}, status=404)
        except Exception as e:
            return JsonResponse({"messsage": "Could not generate rounds"}, status=500)
        
    else:
        return HttpResponse(status=405)
