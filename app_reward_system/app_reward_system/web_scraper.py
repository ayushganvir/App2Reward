from __future__ import absolute_import

from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_reward_system.settings')
app = Celery('app_reward_system', broker='pyamqp://guest@localhost//')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# print(len(titles))
# print(titles)
# print(len(icons))
# print(icons)





