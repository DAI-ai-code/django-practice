from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def insert(request):
    return render(request, 'insert_page3.html')

def delete(request):
    return render(request, 'delete_page3.html')
 

def get_insert_details(request):
    empid = request.POST.get("employeeID")
    ename = request.POST.get("employeeName")
    esalary = request.POST.get("employeeSalary")
    print(ename)
    e = models.Employee(empid, ename, esalary)
    e.save()
    return render(request, 'insert_page3.html')


def del_details(request):
    delID = int(request.POST.get("employeeIDdel"))
    for i in models.Employee.objects.all():
        print('empid',i.empid)
        if i.empid == delID:
            i.delete()
            break

    return render(request, 'delete_page3.html')

