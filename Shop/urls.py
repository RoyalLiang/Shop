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
from django.urls import path, re_path, include
import xadmin
from django.views.static import serve
from Shop.settings import MEDIA_ROOT
from django.conf import settings
from goods.views import *
from other.views import *
from viewsCount.views import *

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name='index'),
    # 文件上传处理函数
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path('mdeditor/', include('mdeditor.urls')),
    path('goods_detail/<int:goods_id>', GoodsDetail.as_view(), name='goods-detail'),
    # path('backend/', BackendIndex.as_view(), name='backend'),
    path('about.html', CompanyIntroduction.as_view(), name='CompanyIntroduction'),
    path('video.html', Video.as_view(), name='Video'),
    path('factory.html', Factory.as_view(), name='Factory'),
    path('customer.html', Customer.as_view(), name='Customer'),
    path('products.html', ProductsList.as_view(), name='ProductsList'),
    path('search.html', Search.as_view(), name='Search'),
    path('message.html', AddMessage.as_view(), name='AddMessage'),
    path('viewscount.html', ViewsCount.as_view(), name='ViewsCount'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
