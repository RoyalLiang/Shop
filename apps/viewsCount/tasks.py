from Shop.celery import app
from .models import Visitor


@app.task
def views_count_save(request):
    if request.META.get('HTTP_X_FORWARDED_FOR', None):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    refer = request.META.get('HTTP_REFERER')
    user_agent = request.META.get('HTTP_USER_AGENT')
    Visitor(ip=ip, refer=refer, user_agent=user_agent).save()
