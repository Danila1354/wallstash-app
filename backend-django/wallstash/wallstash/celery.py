import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wallstash.settings")

app = Celery("wallstash")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
