import smtplib

from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from Announcements.models import Announcements
from Courses.models import Courses
from Log_In.models import Lecturer,RegisteredStaffs, RegisteredStd, StudentsRegister
from django.core.files.storage import FileSystemStorage


# Create your views here.
def makeAnnouncement(request, Staff_No):

    Subject = request.POST['Title']
    Course_Code = request.POST.get('Course Code')

    Content = request.POST['message']



    a = Announcements()
    q = Courses.objects.get(Course_Code=Course_Code[-8:])
    a.Course_Code = q

    p = Lecturer.objects.get(Lect_No=Staff_No)
    a.Lect_No = p

    a.Title = Subject
    a.Content = Content

    a.save()


    TO = []
    arr = RegisteredStd.objects.filter(Course_Code=Course_Code[-8:])
    print(arr)
    for i in arr:
        #print(i.Std_no)
        j = StudentsRegister.objects.filter(Student_No=i.Std_no)
        print(j)
        for k in j:
            print(k.Email)
            if k.Email not in TO:
                TO.append(k.Email)
    print(TO)




    print(Course_Code)

    send_mail(Subject, Content, 'timetablegen19@gmail.com', TO, fail_silently=False)

    print('email sent')

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