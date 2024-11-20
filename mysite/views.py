from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView
from django.urls import path

from services.models import Categories

# Create your views here.


def startpage(request):
    
    # categories = Categories.objects.all()
    
    context = {
        'title': 'Главная страница',
        # 'categories':categories,
    }
    return render(request, 'mysite/startpage.html', context=context)


def loginpage(request):
    context = {
        'title': 'Страница авторизации'
    }
    return render(request, 'mysite/loginpage.html', context=context)

def registration(request):
    context = {
        'title': 'Страница регистрации'
    }
    return render(request, 'mysite/registrationpage.html', context=context)

def pageNotFound(requsest, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')



