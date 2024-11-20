from django import template
from services.models import Categories
from services.models import Services


register = template.Library()


@register.simple_tag()
def tag_categories():
     return Categories.objects.all() 


@register.simple_tag()
def tag_services():
    return Services.objects.all()