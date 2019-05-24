from django.db import models
from Courses.models import Courses
from Log_In.models import Lecturer
# Create your models here.
class Announcements(models.Model):
    Course_Code = models.ForeignKey(Courses, on_delete=models.CASCADE,related_name='Announcements')
    Lect_No = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Content = models.CharField(max_length=100)
    Created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # pdf = models.FileField(upload_to='attachments/pdfs/')


    def __str__(self):
        return str(self.Lect_No) + ' - ' + str(self.Course_Code)