from django.contrib import admin
from .models import SchoolModel

@admin.register(SchoolModel)
class SchoolModelAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'title',
        'description'
    ]
    
