from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def CreateDrawForCompetition(request, competition_id):

    if request.method == 'GET':
        return JsonResponse({'error: Not implimented'}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def GetDrawForCompetition(request, competition_id):

    if request.method == 'GET':
        return JsonResponse({'error: Not implimented'}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
