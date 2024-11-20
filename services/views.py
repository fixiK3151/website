from django.shortcuts import render

from services.models import Services
from services.models import Categories
# Create your views here.


def catalog(request):
    
    # services = Services.objects.all()
    # categories = Categories.objects.all()
    
    
    context = {
        'title':'Домашний интернет',
        # 'services':services,
        # 'categories': categories,
        
    }
    return render(request, 'services/catalog.html', context=context)





def tests(request):
    
    categories = Categories.objects.all()
    
    context = {
        'title':'тестовая страница',
        'categories': categories,
       
    }
    return render(request, 'services/test.html', context=context)