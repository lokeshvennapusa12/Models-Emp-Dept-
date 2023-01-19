from django.db import models

class Dept(models.Model):
    sno=models.IntegerField()
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)

    
class Emp(models.Model):
        sno=models.IntegerField()
        ename=models.CharField (max_length=20, null=True)
        emp_no=models.IntegerField()
        mgr_no=models.IntegerField()
        sal=models.IntegerField(null=True)
        comm=models.IntegerField()
        dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)



