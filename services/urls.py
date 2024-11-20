from django.urls import path
from .views import *

app_name = 'services'

urlpatterns = [
path('', catalog, name='catalog-page'),
path('test/', tests, name='test-page')
]