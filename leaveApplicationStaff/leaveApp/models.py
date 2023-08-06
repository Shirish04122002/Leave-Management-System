from django.db import models

# Create your models here.
class Employees(models.Model):
    userid = models.CharField(max_length=6,primary_key=True, unique=True, default="none")
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, unique=True)
    mobile = models.DecimalField(max_digits=10, decimal_places=0)
    designation = models.CharField(max_length=15)
    location = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    yearsOfExperience = models.IntegerField(null=False, default = 1, blank=False)
    password = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"{self.name} ({self.designation}) - {self.location}"

class Employee_Manager(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    managerId = models.CharField(max_length=6)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return f"Manager ID: {self.managerId}, Employee: {self.employee.name} (ID: {self.employee.id})"

class Staff(models.Model):
    leave_id = models.CharField(max_length=8, default='Pending')
    employeeId = models.CharField(max_length=6, unique=True)
    approverId = models.CharField(max_length=6, null=True)
    address = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=20,null=True)
    leave_type = models.CharField(max_length=15,null=True)
    from_date = models.DateField(null=True) 
    till_date = models.DateField(null=True) 
    reason = models.CharField(max_length=50,null=True)
    approver = models.CharField(max_length=7, default='manager')

    def __str__(self):
        return f"{self.name} - Leave ID: {self.id}"

class Manager(models.Model):
    id = models.CharField(max_length=8, default='Approved', primary_key=True)
    managerId = models.CharField(max_length=6, unique=True)
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    leave_type = models.CharField(max_length=15)
    from_date = models.CharField(max_length=50)
    till_date = models.CharField(max_length=50)
    reason = models.CharField(max_length=50)
    approver = models.CharField(max_length=7, default='HR')

    def __str__(self):
        return f"{self.name} ({self.leave_type}) - {self.from_date} to {self.till_date}"
    
