from . import models

def saver(data):
    e = models.Employee(data['empid'], data['ename'], data['esalary'])
    e.save()
    # return

def deleter(data):
    empid = data['empid']
    x = models.Employee.objects.all()
    for i in x:
        if i.empid == empid:
            i.delete()
            break
    return 

def updater(data):
    empid = data['empid']
    esalary = data['esalary']
    x = models.Employee.objects.all()
    for i in x:
        if i.empid == empid:
            i.emp_salary = esalary
            i.save()
            break
    
    return

def selector(data):
    empid = data['empid']
    for i in models.Employee.objects.all():
        if i.empid == empid:
            return i.__repr__()
