from django.urls import path

from other.views import CompanyIntroduction, Factory, Customer

app_name = 'other'
urlpatterns = [
    path('about.html', CompanyIntroduction.as_view(), name='CompanyIntroduction'),
    path('factory.html', Factory.as_view(), name='Factory'),
    path('customer.html', Customer.as_view(), name='Customer'),
]
