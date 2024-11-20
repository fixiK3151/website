from django.contrib import admin

# Register your models here.

from services.models import Categories, Services

# admin.site.register(Categories)
# admin.site.register(Services)



@admin.register(Categories)
class CatgoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    
    
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)} 