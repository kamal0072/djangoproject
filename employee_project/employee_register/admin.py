from django.contrib import admin
from .models import Emplpoyee,Position

@admin.register(Emplpoyee)
class EmplpoyeeAdmin(admin.ModelAdmin):
    list_display=['id','fullname','emp_code','mobile','position']
    
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display=['id','title']

    
