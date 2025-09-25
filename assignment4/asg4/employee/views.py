import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from . import models, operations
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

def update(request):
    return render(request,'update_page.html')

def update_details(request):
    eid = int(request.POST.get("employeeID"))
    esala = int(request.POST.get("esalary"))

    for i in models.Employee.objects.all():
        if i.empid == eid:
            i.emp_salary = esala
            break
    return render(request,'update_page.html')

def get_emp_details(request):
    data = {"empid":1, "ename":"bbb", "esalary":90000}
    return JsonResponse(data)

@csrf_exempt  #bad practice
def post_emp_details(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    operations.saver(data)
    return JsonResponse(data)

@csrf_exempt
def operations_operator(request):
    data = json.loads(request.body.decode('utf-8'))
    if request.method == 'POST':
        operations.saver(data)
    elif request.method == 'DELETE':
        operations.deleter(data)
    elif request.method == 'PUT':
        operations.updater(data)
    elif request.method == 'GET':
        details = operations.selector(data)
        print(details)
        return JsonResponse(details)
    return JsonResponse(data)