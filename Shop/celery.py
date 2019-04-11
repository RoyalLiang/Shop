from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shop.settings')

# 注册Celery的APP
app = Celery('Shop')
# 绑定配置文件
app.config_from_object('django.conf:settings', namespace='CELERY')
app = Celery('Shop', backend='redis', broker='redis://127.0.0.1:6379/1')
# 自动发现各个app下的tasks.py文件
app.autodiscover_tasks()

app.conf.update(
    CELERY_BROKER_URL='redis://127.0.0.1:6379/1',
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERYD_MAX_TASKS_PER_CHILD=10,
    acks_late=True,
    CELERY_ENABLE_UTC=True,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERYBEAT_SCHEDULE={
        'data_processing': {
            'task': 'viewsCount.tasks.data_processing',
            'schedule': timedelta(minutes=5),
        }
    }
)
