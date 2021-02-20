from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *


def index(request):
    send_email_task()
    return HttpResponse("Done")



