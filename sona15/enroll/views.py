from django.shortcuts import render
from django.http import HttpResponse

from .models import SchoolModel
from .forms import SchoolForm
from django.views.generic.edit import (
                                        CreateView,
                                        DeleteView,
                                        UpdateView,
                                        FormView
                                    )
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

#create View Will Appear Here

class SchoolView(CreateView):
    model=SchoolModel
    fields=[
        'title',
        'description'
    ]
    template_name='enroll/schoolmodel_form.html'

class SchoolListView(ListView):
    model=SchoolModel

class  SchoolDetailView(DetailView):
    model=SchoolModel

class SchoolUpdateView(UpdateView):
    model=SchoolModel
    fields=[
        'title',
        'description'
    ]
    success_url='/'

class SchoolDeletView(DeleteView):
    model=SchoolModel
    success_url='/'

class SchoolFormView(FormView):
    form_class=SchoolForm
    template_name='enroll/schoolform.html'
    success_url='/thanks/'