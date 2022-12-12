# import os
# from celery.schedules import crontab
# from celery import Celery
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krypta.settings')
#
# app = Celery('krypta')
#
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# app.autodiscover_tasks()
# app.conf.beat_schedule = {
#     'parsing': {
#         'task': 'valuta.tasks.parsing_value',
#         'schedule': crontab(minute='*/1'),
#     },
# }
# app.conf.timezone = 'UTC'
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "krypta.settings")
app = Celery("krypta")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'parsing': {
        'task': 'valuta.tasks.parsing_value',
        'schedule': crontab(minute='*/1'),
    },
}
