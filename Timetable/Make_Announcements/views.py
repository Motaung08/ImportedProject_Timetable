from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from Announcements.models import Announcements
from Courses.models import Courses
from Log_In.models import Lecturer,RegisteredStaffs
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from Announcements.forms import AnnouncementsForm



# Create your views here.
def makeAnnouncement(request, Staff_No):

    Subject = request.POST['Title']
    Course_Code = request.POST.get('Course Code')

    Content = request.POST['message']

    PDF = request.POST.get('myfile')

    print(PDF)

    a = Announcements()
    q = Courses.objects.get(Course_Code=Course_Code[-8:])
    a.Course_Code = q

    p = Lecturer.objects.get(Lect_No=Staff_No)
    a.Lect_No = p

    a.Title = Subject
    a.Content = Content

    a.pdf=PDF

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

def upload(request,Staff_No):
    if request.method == 'POST':
        form = AnnouncementsForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            # return redirect('Register/Try.html')
            return render(request, 'Register/Try.html')
    else:
        form = AnnouncementsForm()

    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)
    context = {
        'form': form,
        'STDN': Staff_No,
        'user': user,

    }
    return render(request, 'Register/Try.html', context)
    # return render(request,'Register/Make_Announcement.html',context)