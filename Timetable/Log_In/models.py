from django.db import models
from Courses.models import Courses

# Create your models here.
class StudentsRegister(models.Model):
    Student_No = models.IntegerField()
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Name) + ' - ' + str(self.Student_No)

class Lecturer(models.Model):
    Lect_No = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    CellPhone_No = models.IntegerField()

    def __str__(self):
        return str(self.Name) + ' - ' + str(self.Lect_No)


class RegisteredStaffs(models.Model):
    Staff_no = models.IntegerField(max_length=100)
    Course_Code =models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Staff_no) + ' - ' + str(self.Course_Code)

class RegisteredStd(models.Model):
    Std_no = models.IntegerField(max_length=100)
    Course_Code = models.CharField(max_length=100)


    def __str__(self):
        return str(self.Std_no) + ' - ' + str(self.Course_Code)

class once(models.Model):
    Std_no = models.IntegerField(max_length=100)



    def __str__(self):
        return str(self.Std_no)

