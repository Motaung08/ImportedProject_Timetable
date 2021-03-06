from django.db import models

# Create your models here.
class StudentsRegister(models.Model):
    Student_No = models.IntegerField()
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    CellPhone_No = models.IntegerField()

    def __str__(self):
        return str(self.Name) + ' - ' + str(self.Student_No)


class Login(models.Model):
    Student_No = models.ForeignKey(StudentsRegister, on_delete=models.CASCADE)
    Password = models.IntegerField()


class Lecturer(models.Model):
    Lect_No = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    CellPhone_No = models.IntegerField()

    def __str__(self):
        return str(self.Name) + ' - ' + str(self.Lect_No)

class Courses(models.Model):
    Course_Code = models.CharField(primary_key=True, max_length=100)
    Course_Name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Course_Name) + ' - ' + str(self.Course_Code)


class Announcements(models.Model):
    Course_Code = models.ForeignKey(Courses, on_delete=models.CASCADE)
    Lect_No = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Content = models.CharField(max_length=100)
    Created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.Lect_No) + ' - ' + str(self.Course_Code)

class Class(models.Model):
    Student_No = models.ForeignKey(StudentsRegister, on_delete=models.CASCADE)
    Course_Code = models.ForeignKey(Courses, on_delete=models.CASCADE)
    Lect_No = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    Slot = models.CharField(max_length=100)


    def __str__(self):
        return str(self.Student_No) + ' - ' + self.Lect_No + ' - ' + str(self.Course_Code)

class RegisteredStd(models.Model):
    Std_no = models.IntegerField(max_length=100)
    Course_Code =models.ForeignKey(Courses, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.Std_no) + ' - ' + str(self.Course_Code)

class RegisteredStaffs(models.Model):
    Staff_no = models.IntegerField(max_length=100)
    Course_Code =models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Staff_no) + ' - ' + str(self.Course_Code)



