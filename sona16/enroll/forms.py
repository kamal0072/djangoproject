from django import forms

class SchoolForm(forms.Form):
    name=forms.CharField()
    cell=forms.IntegerField()
    address=forms.Textarea()
