from django.shortcuts import render

# Create your views here.
from .forms import SchoolForm

def home(request):
    form=SchoolForm()
    return render(request,'enroll/index.html',{'form':form})