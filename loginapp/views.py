from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from legosumodb.models import User as LegoSumoUser
from django.views.decorators.csrf import csrf_exempt
import json
import pymysql

def TheModelView(request):

    if request.method == 'GET':

        try:
            data = json.loads(request.body)

            required_fields = ['username', 'password']

            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f"Missing '{field}' in request body"}, status=400)

            username = data.get('username')
            password = data.get('password')

            user = LegoSumoUser.objects.get(username=username, password=password)
            response_data = {
                'role': user.role
            }

            return JsonResponse(response_data)

        except LegoSumoUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        except Exception as e:
            return JsonResponse({'error': 'An error occurred'}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

