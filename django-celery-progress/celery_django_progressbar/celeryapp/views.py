from django.shortcuts import render
from time import sleep

from .tasks import*

# start celery server =celery -A projectname  worker -l  info

def index(request):
    go_to_sleepy(5)
    task =  go_to_sleepy.delay(5)
    return render(request, 'views/index.html',{'task_id': task.task_id})
