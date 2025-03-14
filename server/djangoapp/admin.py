from django.contrib import admin
from .models import CarMake, CarModel


# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'description')
    search_fields = ('name', 'country')
    list_filter = ('country',)


# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'fuel_type')
    search_fields = ('name', 'car_make__name')
    list_filter = ('type', 'year', 'fuel_type')
    list_select_related = ('car_make',)


# Register models with admin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
