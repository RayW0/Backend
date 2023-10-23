from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatLog
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


@csrf_exempt
def create_chat_log(request):
    print(request.GET.get('message'))
    message = request.GET.get('message')
    date_of_creation = datetime.now().strftime('%d.%m.%Y %H:%m')
    try:
        ChatLog.objects.create(
            message=message, 
            date_of_creation=date_of_creation,
            )
        return JsonResponse({'res': 'success'})
    except:
        return JsonResponse({'res': 'error'})

@csrf_exempt
def get_chat_log(request):
    chat_logs = ChatLog.objects.values()
    try:
        return JsonResponse({'res': 'success', 'chat_logs': list(chat_logs)}, safe=False)
    except:
        return JsonResponse({'res': 'error'})
        