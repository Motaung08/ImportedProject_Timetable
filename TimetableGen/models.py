from django.db import models

# Create your models here.
class StudentsRegister(models.Model):
    Student_No = models.IntegerField()
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    CellPhone_No = models.CharField(max_length=13)


class Login(models.Model):
    Student_No = models.ForeignKey(StudentsRegister, on_delete=models.CASCADE)
    Password = models.CharField(max_length=100)