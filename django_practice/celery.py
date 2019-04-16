from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_practice.settings')
 
app = Celery('django_practice')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()