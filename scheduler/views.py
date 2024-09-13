from django.http import JsonResponse, HttpResponse
from .tasks import add

def default_scheduler(request):
    return JsonResponse({"message": "Hello from task scheduler"})

def task(request):
    add.delay()
    return HttpResponse("Task Started!")
