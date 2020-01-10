import os
from celery import Celery

# задаём переменную окружения, содержащую название файла настроек нашего проекта
# 229
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
