from django.shortcuts import get_object_or_404, render
from .forms import StudentForm
from .models import StudentModel
from django.forms import formset_factory

# def formset_view(request):
#     context ={}
  
#     # creating a formset and 5 instances of GeeksForm
#     GeeksFormSet = formset_factory(EnrollForm, extra = 3)
#     formset = GeeksFormSet(request.POST or None)
      
#     # print formset data if it is valid
#     if formset.is_valid():
#         for form in formset:
#             print(form.cleaned_data)
              
#     # Add the formset to context dictionary
#     context['formset']= formset
#     return render(request, "enroll/home.html", context)

# def home_view(request):
#     # create a dictionary to pass
#     # data to the template
#     context ={
#         "data":"Gfg is the best",
#         "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     }
#     # return response with template and context
#     return render(request, "enroll/about.html", context)

import datetime
from django.http import HttpResponse
def home_time(request):
    ct=datetime.datetime.now()
    html="The Current TIme is {}". format(ct)
    return HttpResponse(html)

from .models import StudentModel
from django.views.generic.list import ListView
from django.http.response import HttpResponseRedirect

# class StudentListView(ListView):
#     model=StudentModel


def create_view(request):
        # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
          
    context['form']= form
    return render(request, "enroll/create_view.html", context)

def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["dataset"] = StudentModel.objects.all()
          
    return render(request, "enroll/list_view.html", context)

def detail_view(request,id):
    context ={}
  
    # add the dictionary during initialization
    context["data"] = StudentModel.objects.get(id = id)
          
    return render(request, "enroll/detail_view.html", context)

def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
   
    # add the dictionary during initialization
    context["data"] = StudentModel.objects.get(id = id)
           
    return render(request, "enroll/detail_view.html", context)


# from django.http import 

def update_view(request, id):
    context ={}
    obj = get_object_or_404(StudentModel, id = id)
    form = StudentModel(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"] = form
    return render(request, "enroll/update_view.html", context)
def delete_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # fetch the object related to passed id
    obj = get_object_or_404(StudentModel, id = id)
  
  
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")
  
    return render(request, "enroll/delete_view.html", context)