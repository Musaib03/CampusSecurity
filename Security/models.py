from django.db import models

# Create your models here.
from django.db import models

class Block(models.Model):
    BlockID = models.AutoField(primary_key=True)
    BlockName = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)

    def __str__(self):
        return self.BlockName

class Shift(models.Model):
    ShiftID = models.AutoField(primary_key=True)
    ShiftName = models.CharField(max_length=50)
    StartTime = models.TimeField()
    EndTime = models.TimeField()

    def __str__(self):
        return self.ShiftName

class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    DOB = models.DateField()
    Gender = models.CharField(max_length=10)
    Address = models.TextField()
    Phone = models.CharField(max_length=15)
    Email = models.EmailField()
    Position = models.CharField(max_length=50)
    DateHired = models.DateField()

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Assignment(models.Model):
    AssignmentID = models.AutoField(primary_key=True)
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    BlockID = models.ForeignKey(Block, on_delete=models.CASCADE)
    ShiftID = models.ForeignKey(Shift, on_delete=models.CASCADE)
    DayOfWeek = models.CharField(max_length=10)

    def __str__(self):
        return f"Assignment {self.AssignmentID}"

class Attendance(models.Model):
    AttendanceID = models.AutoField(primary_key=True)
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Date = models.DateField()
    CheckInTime = models.TimeField()
    CheckOutTime = models.TimeField()

    def __str__(self):
        return f"Attendance {self.AttendanceID} for {self.EmployeeID}"

class Leave(models.Model):
    LeaveID = models.AutoField(primary_key=True)
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    LeaveType = models.CharField(max_length=20)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Reason = models.TextField()
    Status = models.CharField(max_length=20)

    def __str__(self):
        return f"Leave {self.LeaveID} for {self.EmployeeID}"
