from django.db import models

# Create your models here.
class Employee(models.Model):
	eid=models.CharField(max_length=10)
	ename=models.CharField(max_length=20)
	eemail=models.EmailField()	

	class Meta:
		db_table="employee"
		verbose_name_plural="employeeee"