# celery.py

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OCR.settings')

app = Celery('OCR')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

## celery -A OCR.celery worker --loglevel=info