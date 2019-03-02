from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views


register_converter(FourDigitYearConverter, 'year')

app_name = 'shop'
urlpatterns = [
    path('', views.item_list),
    path('archives/<year:year>/', views.archives_year),
]
