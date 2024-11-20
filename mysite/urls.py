from django.urls import path
from .views import *

app_name = 'mysite'

urlpatterns = [
path('', startpage, name='start-page'),
path('login/', loginpage, name='login-page'),
path('registration/', registration, name='regs-page')
]