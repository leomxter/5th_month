from django.contrib import admin

from apps.cars.models import Car, SpecialMarks, PeriodsOwnership

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'color', 'rudder_location']
    # fields = ['brand', 'model']
    list_filter = ['brand', 'model', 'year', 'color', 'rudder_location']
    list_per_page = 20
    search_fields = ['brand', 'model', 'year', 'color', 'rudder_location']

@admin.register(SpecialMarks)
class SpecialMarksAdmin(admin.ModelAdmin):
    list_display = ['car', 'title']
    list_filter = ['car', 'title']
    list_per_page = 20
    search_fields = ['car__brand', 'title']

@admin.register(PeriodsOwnership)
class PeriodsOwnershipAdmin(admin.ModelAdmin):
    list_display = ['car', 'from_date', 'before_date']
    list_filter = ['car', 'from_date', 'before_date']
    list_per_page = 20
    search_fields = ['car__brand', 'from_date', 'before_date']