from celery import shared_task

from time import sleep
from django.core.email import send_mail


# celery command - celery -A django_email_celery worker -1  info
@shared_task
def sleepy(duration):
    sleep.delay(duration)
    return None


@shared_task
def send_email_task():
    sleepy(10)
    send_mail('Celery  Task  Worked!','This is proof the task worked!',
    'vivke@gmail.com',
    ['sasa@be-breathtaking.net']
    )
    return None