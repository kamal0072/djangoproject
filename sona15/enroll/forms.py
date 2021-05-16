from django import forms
from .models import SchoolModel
class SchoolForm(forms.ModelForm):
    class Meta:
        model=SchoolModel
        fields=[
            'id',
            'title',
            'description'
        ]