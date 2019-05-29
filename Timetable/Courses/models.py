from django.db import models

# Create your models here.

class Courses(models.Model):
    Course_Code = models.CharField(primary_key=True, max_length=100)
    Course_Name = models.CharField(max_length=100)
    Course_Diagonal = models.CharField(max_length=100, default='Null')
    Course_Semester = models.CharField(max_length=100, default='Null')
    Course_TimeSlot = models.CharField(max_length=100, default='Null')
    Course_Day = models.CharField(max_length=100, default='Null')
    # pdf = models.FileField(upload_to='attachments/pdfs/')

    def __str__(self):
        return str(self.Course_Name) + ' - ' + str(self.Course_Code)
