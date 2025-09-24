from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField(default=0)
    ename = models.CharField(max_length=200)
    salary=models.IntegerField(default=0)