from django.db import models

# Create your models here.
class LectureRegister(models.Model):
    Stuffnumber = models.IntegerField()
    Initials = models.CharField(max_length=5)
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    CellPhone_No = models.IntegerField()


class Login(models.Model):
    Stuffnumber = models.ForeignKey(LectureRegister, on_delete=models.CASCADE)
    Password = models.IntegerField()
