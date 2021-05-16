from django.contrib import admin
from .models import StudentModel

@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['id','title','description']
    
