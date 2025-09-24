from django.db import models

# Create your models here.
class Manager(models.Model):
    manager_id = models.IntegerField(default=0, primary_key=True)
    manager_name = models.CharField(max_length=200)
    manager_salary = models.IntegerField(default=0)
    #UPSERT -> agr inserted h to update vrna insert. Not a sql query!!

    def __str__(self):
        return f'Manager ID : {self.manager_id}, manager name : {self.manager_name}'
