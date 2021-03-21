from celery import shared_task
from celery_progress.backend import ProgressRecorder
from time import sleep



# celery command - celery -A django_email_celery worker -1  info
@shared_task(bind=True)
def go_to_sleepy(self,duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(5):
        sleep.delay(duration)
        progress_recorder.set_progress(i+1,5, f'On iteration {i}')
    return None

