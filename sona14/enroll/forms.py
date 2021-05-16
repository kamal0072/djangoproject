from django import forms
from django.forms import formset_factory
from .models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields=[
            'title',
            'description'
        ]