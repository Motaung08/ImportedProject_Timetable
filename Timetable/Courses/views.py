from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from .models import  Courses
from Log_In.models import StudentsRegister, Lecturer,RegisteredStaffs,RegisteredStd
from Courses.models import Courses

from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def courses(request, STDN):

    print("inside function")


    user = RegisteredStd.objects.filter(Std_no=STDN)
    # course = list(Courses.objects.all())
    # print(course[1])
    # ad= str(course[1])
    # #print(user.Course_Code)
    # #print(user.Course_Code)
    # #user.Course_Code
    # for i in user:
    #     i.Course_Code
    #     print(i.Course_Code)
    #
    #
    # if(ad[-8:] == "COMS3003"):
    #     print("yes")
    # print("hello")
    #
    # print("below s")
    #
    # for i in user:
    #     g = str(i.Course_Code)
    #     for k in range(0,len(course)):
    #         ad = str(course[k])
    #         if (ad[-8:] == g):
    #             print("yessssssssssssssssss")
    #             print(ad)
    #
    #
    #

    context = {
        'user': user,
        'STDN': STDN,
        #"course": course
    }
    print("inside function")
    # simple_upload(request)

    return render(request, 'Register/Courses.html', context)

def StaffCourses(request, Staff_No):
    print("inside function")

    # if request.method == 'POST':
    #     form = CoursesForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = CoursesForm()

    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)

    print("below s")
    context = {
        # 'form': form,
        'user': user,
        'STDN': Staff_No,

    }
    print("inside function")

    #return HttpResponse("<h1> Hello</h1>")
    return render(request, 'Register/Courses.html', context)