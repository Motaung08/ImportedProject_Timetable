from django import forms

from .models import Announcements


class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ('Course_Code', 'Lect_No','Title','Content', 'pdf')
