from django import forms

from .models import Announcements,Courses


class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ('Course_Code', 'Content','Lect_No', 'pdf')


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('Course_Code', 'Course_Name','pdf')