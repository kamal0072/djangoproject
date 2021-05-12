from django import forms
from .models import Emplpoyee,Position
from crispy_forms.helper import FormHelper
from crispy_forms import helper
from crispy_forms.layout import Submit 
from django.forms import TextInput,NumberInput
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Emplpoyee
        fields=['fullname','emp_code','mobile','position']
        labels={'fullname':'Full Name','emp_code':'Employee Code',
        'mobile':'Mobile Number','position':'Position'}
        widgets = {
            "fullname":TextInput(attrs={"placeholder": "Please Enter Your Full Name Here---"}),
            "emp_code":TextInput(attrs={'placeholder':'Enter Your Employee Code Here---'}),
            "mobile":NumberInput(attrs={'placeholder':'Enter Your correct Cell Number---'})}
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "--Select--"
       