# admin.py
from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'height', 'weight', 'blood_pressure', 'cholesterol_levels')
    list_filter = ('age', 'height', 'weight', 'blood_pressure', 'cholesterol_levels')
    search_fields = ('name', 'age', 'height', 'weight', 'blood_pressure', 'cholesterol_levels')

admin.site.register(Person, PersonAdmin)