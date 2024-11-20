from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию услуг'
        verbose_name_plural = 'Категории услуг'
    
    def __str__(self):
        return self.name
    
       
        
        
class Services(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    tarifexternalname = models.CharField(max_length=150, unique=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория услуг')
    
    class Meta:
        db_table = 'service'
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
        
    def __str__(self):
        return self.name
