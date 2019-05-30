from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from .models import  Courses
from Log_In.models import StudentsRegister, Lecturer,RegisteredStaffs,RegisteredStd

from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def courses(request, STDN):

    print("inside function")


    user = RegisteredStd.objects.filter(Std_no=STDN)

    print("below s")
    context = {
        'user': user,
        'STDN': STDN,
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