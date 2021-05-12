from django.shortcuts import render,redirect
from .models import Position,Emplpoyee
from .forms import EmployeeForm
# Create your views here.
def employee_list(request):
    context={'employe_list':Emplpoyee.objects.all()}
    return render(request,'employee_register/employee_list.html',context)

def employee_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form=EmployeeForm()
        else:
            employee=Emplpoyee.objects.get(pk=id)
            form=EmployeeForm(instance=employee)    
        return render(request,'employee_register/employee_form.html',{'form':form})
    else:
        if id==0:
            form=EmployeeForm(request.POST)
        else:    
            employee=Emplpoyee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list/')     


from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)

def employee_delete(request, id):
    context ={}
    obj = get_object_or_404(Emplpoyee, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/employee/list/")
    return render(request, "employee_register/delete_view.html", context)
  
  
  