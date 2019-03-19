from django.urls import path

from other.views import CompanyIntroduction_view, Factory_view, Customer_view, Video_view, News_view, News_detail

app_name = 'other'
urlpatterns = [
    path('about.html', CompanyIntroduction_view.as_view(), name='CompanyIntroduction'),
    path('video.html', Video_view.as_view(), name='Video'),
    path('factory.html', Factory_view.as_view(), name='Factory'),
    path('customer.html', Customer_view.as_view(), name='Customer'),
    path('news.html', News_view.as_view(), name='News'),
    path('news<int:news_id>.html', News_detail.as_view(), name='NewsDetail'),
]
