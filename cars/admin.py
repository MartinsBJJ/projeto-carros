from django.contrib import admin
from cars.models import Car, Brand

class BrandAdmin (admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year','model_year','value')
    search_fields = ('model',)
    ordering = ('-factory_year',) ##ordena do mais recente pro mais antigo

admin.site.register(Car, CarAdmin)
