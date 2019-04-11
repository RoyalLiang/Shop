"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from Shop.settings import MEDIA_ROOT
from django.conf import settings

from goods.views import IndexView
from viewsCount.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    # 文件上传处理函数
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path('mdeditor/', include('mdeditor.urls')),
    path('goods/', include('goods.urls', namespace='goods')),
    path('other/', include('other.urls', namespace='other')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('viewscount.html', ViewsCount.as_view(), name='ViewsCount'),
    path('viewsCount/', include('viewsCount.urls', namespace='viewsCount'))
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = '伊特纳(天津)科技发展有限公司'
admin.site.site_title = '伊特纳(天津)科技发展有限公司后台管理'
