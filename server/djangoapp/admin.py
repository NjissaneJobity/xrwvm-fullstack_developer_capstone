from django.contrib import admin
from .models import CarMake, CarModel

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'description')  # Columns to display in the list view
    search_fields = ('name', 'country')  # Fields to search by
    list_filter = ('country',)  # Filter by country

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'fuel_type')  # Columns to display
    search_fields = ('name', 'car_make__name')  # Search by model name and car make name
    list_filter = ('type', 'year', 'fuel_type')  # Filters for type, year, and fuel type
    list_select_related = ('car_make',)  # Optimize queries by pre-fetching car_make

# Register models with admin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
