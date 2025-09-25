from django.db import models
from . import views
# Create your models here.


class Employee(models.Model):

    empid = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=200)
    emp_salary = models.IntegerField(default=0)

    def __repr__(self):
        return {'empid' : self.empid, 'ename' : self.emp_name, 'emp_salary' : self.emp_salary}

