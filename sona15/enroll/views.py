from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)
from django.views.generic.list import ListView

from .forms import SchoolForm
from .models import SchoolModel

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

import demjson


class SchoolFormView(FormView):
    # storing marks of 3 subjects
    var = [{"Math": 50, "physics":60, "Chemistry":70}]
    print(demjson.encode(var))

    form_class=SchoolForm
    template_name='enroll/schoolform.html'
    success_url='/thanks/'

import json
import urllib.request
def index(request):
    if request.method=="POST":
        city=request.POST['city']
        source = urllib.request.urlopen(
        'http://api.openweathermap.org/data/2.5/weather?q =' 
                + city + '&appid = your_api_key_here').read()

        list_of_data=json.loads(source)

        data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' '
                    + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data={}
    return render(request,'enroll/index.html',{'data':data})        