from apiproject.celery import app as celery_app
from celery import shared_task

import time

@celery_app.task
def test():
    pass

@shared_task
def add(x, y):
    print('call add function.')
    time.sleep(2)
    return x + y