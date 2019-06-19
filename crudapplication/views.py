from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def enter(request):
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("crudapplication:show")
	form=EmployeeForm()
	return render(request,"main/enter.html",{'form':form})

def show(request):
	employee = Employee.objects.all()
	return render(request,"main/show.html",{'employee':employee})

def edit(request,id):
	employee=Employee.objects.get(id=id)
	return render(request,"main/edit.html",{'employee':employee})

def update(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("crudapplication:show")
	
	return render(request,"main/edit.html",{'employee':employee})

def delete(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect("crudapplication:show")