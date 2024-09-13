from django.urls import path
from .views import default_scheduler, task

urlpatterns = [
    path('', default_scheduler),
    path('task', task, name="task")
]