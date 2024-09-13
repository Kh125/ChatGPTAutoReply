from celery import Celery, shared_task
from time import sleep

@shared_task(bind=True)
def add(self):
    for i in range(10):
        print(i)
    print("Task Completed!")