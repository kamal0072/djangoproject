from django import forms

class EnrollForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()
