from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from Announcements.models import Announcements
from Courses.models import Courses
from Log_In.models import Lecturer,RegisteredStaffs
from django.core.files.storage import FileSystemStorage


# Create your views here.
def makeAnnouncement(request, Staff_No):

    Subject = request.POST['Title']
    Course_Code = request.POST.get('Course Code')

    Content = request.POST['message']



    print(Staff_No)


    a = Announcements()
    q = Courses.objects.get(Course_Code=Course_Code[-8:])
    a.Course_Code = q

    p = Lecturer.objects.get(Lect_No=Staff_No)
    a.Lect_No = p

    a.Title = Subject
    a.Content = Content

    a.save()

    print("Done")
    return render(request, 'Register/Announcement.html')

def make(request,Staff_No):
    print(Staff_No)
    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)

    print(user)
    context = {
        'user': user,
        'STDN': Staff_No,

    }
    return render(request, 'Register/Make_Announcement.html',context)