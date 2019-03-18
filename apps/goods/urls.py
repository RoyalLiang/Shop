from django.urls import path

from .views import GoodsDetail, IndexView, ProductsList, Search, AddMessage
from .models import Video

app_name = 'goods'
urlpatterns = [
    path('goods_detail/<int:goods_id>', GoodsDetail.as_view(), name='goods-detail'),
    path('video.html', Video, name='Video'),
    path('products.html', ProductsList.as_view(), name='ProductsList'),
    path('search.html', Search.as_view(), name='Search'),
    path('message.html', AddMessage.as_view(), name='AddMessage'),

]
